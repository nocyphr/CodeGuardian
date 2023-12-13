from os.path import exists
from src.report import generate_report

def test_that_report_file_is_created():
    generate_report('no/path')
    assert exists('./output/report.json')