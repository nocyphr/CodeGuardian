Feature: generate_report

  In order to improve my code
  As a software developer
  I want to get a code review report

  Scenario Outline: report is generated in output folder
    Given a file in the input folder "./input/code_file.py"
    When I analyze the file
    Then i find a json file "./output/report.json"
    And the datapoint <datapoint> contains <data>

    Examples:
      | datapoint | data                  |
      | path      | ./input/code_file.py  |
      | avg_cc    | 2.0                   |
      | total_cc  | 4.0                   |

