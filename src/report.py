from os.path import exists
from lizard import analyze_file
from json import dump
import re



class FileHandler:
    def __init__(self, file_path: str):
        self.max_file_lines: int = 500
        self.file_content: str = ''

        self.file_path: str = file_path
        self.read_file()
        self.analysis_results = analyze_file(self.file_path)

    def read_file(self) -> str:
        if not exists(self.file_path):
            raise FileNotFoundError(f'No file found at {self.file_path}')

        with open(self.file_path) as file:
            self.file_content = file.read()

        if not self.file_content.strip():
            raise ValueError(f'File {self.file_path} did not contain code')

    def count_lines(self) -> int:
        regex_pattern = r'^(?!\s*$)(?!\s*#).+'
        matches = re.findall(regex_pattern, self.file_content, re.MULTILINE)
        return len(matches)

    def calculate_avg_cc(self) -> float:
        return self.analysis_results.average_cyclomatic_complexity

    def calculate_total_cc(self) -> float:
        cc_per_function: list = [function.cyclomatic_complexity for function in self.analysis_results.function_list]
        return float(sum(cc_per_function))

    def create_report_dict(self) -> dict:
        code_lines: int = self.count_lines()

        report_dict: dict = {'path': self.file_path}
        report_dict['avg_cc'] = self.calculate_avg_cc()
        report_dict['total_cc'] = self.calculate_total_cc()
        report_dict['lines_over_max'] = '-' if code_lines < self.max_file_lines else code_lines - self.max_file_lines

        return report_dict


def write_file(output_path: str, data: dict):
    with open(output_path, 'w') as file:
        dump(data, file, indent=4)


def generate_report(file_path: str, output_path='./output/report.json'):
    file_handler = FileHandler(file_path)
    report_dict = file_handler.create_report_dict()
    write_file(output_path, report_dict)


# Example usage:
# generate_report("./src/report.py")
