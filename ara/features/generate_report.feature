Feature: generate_report

  In order to improve my code
  As a software developer
  I want to get a code review report

  Scenario: report is generated in output folder
    Given a code file "./input/code_file.py"
    When I analyze the code file
    Then I find a json file "./output/report.json"
    

  Scenario Outline: report contains expected data
    Given a report file "./output/report.json"
    When I read the report file
    Then the datapoint <datapoint> contains <data>

    Examples:
      | datapoint | data                  |
      | path      | ./input/code_file.py  |
      | avg_cc    | 2.0                   |
      | total_cc  | 4.0                   |

  Scenario Outline: report contains lines_over_max if long file was input
    Given a report file "./output/report.json"
    And a code file "<input_file_path>"
    When I analyze the code file
    And I read the report file
    Then the datapoint <datapoint> contains <data>

    Examples: 
    | input_file_path       | datapoint           | data  |
    | ./input/code_file.py  | lines_over_max      | -     |
    | ./input/big_file.py   | lines_over_max      | 449   |
    | ./input/big_file.py   | functions_over_max  | -     |


# given code_file.py, when I analyze my bla, and I read bla, then there is a list of examples of each function and its parameters


  Scenario Outline: report contains lines_over_max if long file was input
    Given a report file "./output/report.json"
    And a code file "<input_file_path>"
    When I analyze the code file
    And I read the report file
    Then there is a function <function_name> with the datapoint <datapoint> containing <data>

    Examples: 
    | input_file_path       | function_name | datapoint           | data  |
    | ./input/code_file.py  | main          | lines_over_max      | 3     |
    | ./input/code_file.py  | main          | cc                  | 1     |
    | ./input/code_file.py  | main          | parameters_over_max | -     |
    | ./input/big_file.py   | make_subplots | lines_over_max      | 372   |
    | ./input/big_file.py   | make_subplots | cc                  | 106   |
    | ./input/big_file.py   | make_subplots | parameters_over_max | 17    |