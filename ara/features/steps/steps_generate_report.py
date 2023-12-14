from os.path import exists
from src.report import generate_report
from json import load

@given(u'a report file "{input_file_path}"')
def step_impl(context, input_file_path):
    context.report_file_path = input_file_path

@given(u'a code file "{input_file_path}"')
def step_impl(context, input_file_path):
    context.code_file_path = input_file_path


@when(u'I analyze the code file')
def step_impl(context):
    generate_report(context.code_file_path)


@then(u'i find a json file "{output_file_path}"')
def step_impl(context, output_file_path):
    assert exists(output_file_path), f'file: {output_file_path} was not found'

@when(u'I read the report file')
def step_impl(context):
    with open (context.report_file_path) as file: 
        context.report_dict = load(file)


@then(u'the datapoint {datapoint} contains {data}')
def step_impl(context, datapoint, data):
    assert str(context.report_dict[datapoint]) == data