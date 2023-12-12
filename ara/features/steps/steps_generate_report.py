@given(u'a file in the input folder "{input_file_path}"')
def step_impl(context, input_file_path):
    raise NotImplementedError(u'STEP: Given a file in the input folder "./input/code_file.py"')


@when(u'I analyze the file')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I analyze the file')


@then(u'i find a json file "{output_file_path}"')
def step_impl(context, output_file_path):
    raise NotImplementedError(u'STEP: Then i find a json file "./output/report.json"')


@then(u'the datapoint {datapoint} contains {data}')
def step_impl(context, datapoint, data):
    raise NotImplementedError(u'STEP: Then the datapoint {datapoint} contains {data}')