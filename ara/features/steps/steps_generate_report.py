from os.path import exists
from src.report import generate_report

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
    raise NotImplementedError(u'STEP: When I read the file')


@then(u'the datapoint {datapoint} contains {data}')
def step_impl(context, datapoint, data):
    raise NotImplementedError(u'STEP: Then the datapoint {datapoint} contains {data}')