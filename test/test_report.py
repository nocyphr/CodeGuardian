from os.path import exists
from json import load
from src.report import generate_report, read_file
from pytest import raises



def test_that_report_file_is_created():
    generate_report('./input/code_file.py')
    assert exists('./output/report.json')


def test_that_generate_report_fails_for_invalid_input_path():
    invalid_path = 'invalid/path'
    with raises(FileNotFoundError) as e:
        generate_report(invalid_path)
    assert f'no file found at {invalid_path}' in str(e.value)

def test_that_read_file_returns_non_empty_string():
    result: str = read_file('./input/code_file.py')
    assert len(result) > 0