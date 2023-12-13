from os.path import exists

def generate_report(file_path):
    if not exists(file_path):
        raise FileNotFoundError(f'no file found at {file_path}')
    with open('./output/report.json', 'w'):
        ...
