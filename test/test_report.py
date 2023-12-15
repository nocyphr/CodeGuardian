from os.path import exists
from json import load
from src.report import generate_report, FileHandler
from pytest import raises

# Adjust the tests to use FileHandler

def test_that_report_file_is_created():
    generate_report('./input/code_file.py')
    assert exists('./output/report.json')

def test_that_generate_report_fails_for_invalid_input_path():
    invalid_path = 'invalid/path'
    with raises(FileNotFoundError) as e:
        FileHandler(invalid_path)
    assert f'No file found at {invalid_path}' in str(e.value)

def test_that_filehandler_initializes_correctly():
    file_handler = FileHandler('./input/code_file.py')
    assert len(file_handler.file_content) > 0

def test_that_filehandler_raises_error_for_empty_file():
    empty_file_path = './input/empty_file.py'
    with raises(ValueError) as e:
        FileHandler(empty_file_path)
    assert f'File {empty_file_path} did not contain code' in str(e.value)

def test_that_filehandler_creates_correct_report_dict():
    file_handler = FileHandler('./input/code_file.py')
    report_dict = file_handler.create_report_dict()
    assert report_dict['path'] == './input/code_file.py'

def test_that_filehandler_calculates_correct_avg_cc():
    file_handler = FileHandler('./input/code_file.py')
    assert file_handler.calculate_avg_cc() == 2.0

def test_that_filehandler_calculates_correct_total_cc():
    file_handler = FileHandler('./input/code_file.py')
    assert file_handler.calculate_total_cc() == 4.0

def test_that_filehandler_counts_lines_correctly():
    file_handler = FileHandler('./input/code_file.py')
    assert isinstance(file_handler.count_lines(), int)

def test_that_filehandler_counts_correct_number_of_lines():
    file_handler = FileHandler('./input/big_file.py')
    assert file_handler.count_lines() == 1159

def test_that_filehandler_counts_correct_number_of_lines2():
    file_handler = FileHandler('./input/code_file.py')
    assert file_handler.count_lines() == 35
