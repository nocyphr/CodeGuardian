from os.path import exists



def read_file(file_path: str) -> str: 
    if not exists(file_path):
        raise FileNotFoundError(f'no file found at {file_path}')

    with open(file_path) as file: 
        file_content: str = file.read()

    if not file_content.strip():
        raise Exception(f'file {file_path} did not contain code')
    return file_content


def generate_report(file_path: str):
    code_content: str = read_file(file_path)

    with open('./output/report.json', 'w'):
        ...
