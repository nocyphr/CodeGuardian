from os.path import exists
from src.report import generate_report
from json import load

@given(u'a file "{input_file_path}"')
def step_impl(context, input_file_path):
    context.input_file_path = input_file_path


@when(u'I analyze the file')
def step_impl(context):
    generate_report(context.input_file_path)


@then(u'i find a json file "{output_file_path}"')
def step_impl(context, output_file_path):
    assert exists(output_file_path), f'file: {output_file_path} was not found'

@when(u'I read the file')
def step_impl(context):
    with open (context.input_file_path) as file: 
        context.report_dict = load(file)


@then(u'the datapoint {datapoint} contains {data}')
def step_impl(context, datapoint, data):
    assert str(context.report_dict[datapoint]) == data