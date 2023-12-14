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

  # Scenario Outline: report contains lines_over_max if long file was input
  #   Given a report file "./output/report.json"
  #   And a code file <input_file_path>
  #   When I analyze the file
  #   And I read the file
  #   Then "lines_over_max"

