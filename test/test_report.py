from os.path import exists
from json import load
from src.report import generate_report
from pytest import raises



def test_that_report_file_is_created():
    generate_report('no/path')
    assert exists('./output/report.json')


def test_that_generate_report_fails_for_invalid_input_path():
    invalid_path = 'invalid/path'
    with raises as e:
        generate_report(invalid_path)
    assert f'no file found at {invalid_path}' in e.value 
