from os.path import exists
from lizard import analyze_file
from json import dump
import re



class FileHandler:
    def __init__(self, file_path: str):
        self.max_file_lines: int = 500
        self.max_functions: int = 50
        self.file_content: str = ''
        self.max_function_lines: int = 15
        self.max_parameters: int = 3

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

    def calculate_diff_from_max(self, analysis_result: int, max_number: int) -> int:
        if analysis_result < max_number: 
            return '-'
        if analysis_result >= max_number: 
            return analysis_result - max_number


    def create_functions_report(self): 
        report_dict = {'functions': {}}
        for function in self.analysis_results.function_list:
            report_dict['functions'][function.name] = {
                'cc': function.cyclomatic_complexity, 
                'lines_over_max': self.calculate_diff_from_max(function.nloc, self.max_function_lines),
                'parameters_over_max': self.calculate_diff_from_max(function.parameter_count, self.max_parameters)
            }
        return report_dict['functions']

    def count_functions(self) -> int:
        return len(self.analysis_results.function_list)

    def count_lines(self) -> int:
        return self.analysis_results.nloc

    def calculate_avg_cc(self) -> float:
        return self.analysis_results.average_cyclomatic_complexity

    def calculate_total_cc(self) -> float:
        cc_per_function: list = [function.cyclomatic_complexity for function in self.analysis_results.function_list]
        return float(sum(cc_per_function))

    def create_report_dict(self) -> dict:
        code_lines: int = self.count_lines()
        function_number: int = self.count_functions()

        report_dict: dict = {'path': self.file_path}
        report_dict['avg_cc'] = self.calculate_avg_cc()
        report_dict['total_cc'] = self.calculate_total_cc()
        report_dict['lines_over_max'] = self.calculate_diff_from_max(analysis_result=code_lines, max_number=self.max_file_lines)
        report_dict['functions_over_max'] = self.calculate_diff_from_max(analysis_result=function_number, max_number=self.max_functions)
        report_dict['functions'] = self.create_functions_report()
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
