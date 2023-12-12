@given(u'a file in the input folder "./input/code_file.py"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a file in the input folder "./input/code_file.py"')


@when(u'I analyze the file')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I analyze the file')


@then(u'i find a json file "./output/report.json"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i find a json file "./output/report.json"')


@then(u'the datapoint path contains ./input/code_file.py')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the datapoint path contains ./input/code_file.py')


@then(u'the datapoint avg_cc contains 2.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the datapoint avg_cc contains 2.0')


@then(u'the datapoint total_cc contains 4.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the datapoint total_cc contains 4.0')