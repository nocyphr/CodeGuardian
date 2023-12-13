from os.path import exists
from json import dump

from lizard import analyze_file


def read_file(file_path: str) -> str: 
    if not exists(file_path):
        raise FileNotFoundError(f'no file found at {file_path}')

    with open(file_path) as file: 
        file_content: str = file.read()

    if not file_content.strip():
        raise Exception(f'file {file_path} did not contain code')
    return file_content

def add_path_to_report_dict(file_path: str) -> dict: 
    return {'path': file_path}

def calculate_avg_cc(file_path: str) -> float: 
    analysis_results: object = analyze_file(file_path)
    avg_cc: float = analysis_results.average_cyclomatic_complexity
    return avg_cc


def calculate_total_cc(file_path: str) -> float: 
    analysis_results: object = analyze_file(file_path)
    cc_per_function: list = [function.cyclomatic_complexity for function in analysis_results.function_list]
    total_cc: float = float(sum(cc_per_function))
    return total_cc


def generate_report(file_path: str, output_path='./output/report.json'):
    report_dict: dict = add_path_to_report_dict(file_path)
    report_dict['avg_cc'] = calculate_avg_cc(file_path)
    report_dict['total_cc'] = calculate_total_cc(file_path)
    code_content: str = read_file(file_path)


    with open(output_path, 'w') as file:
        dump(report_dict, file, indent=4)


if __name__ == '__main__': 
    generate_report('./src/report.py')