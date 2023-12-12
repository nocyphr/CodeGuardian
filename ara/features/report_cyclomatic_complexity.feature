Feature: Calculate Cyclomatic Complexity from Control Flow Graph

  As a software developer
  I want to calculate the cyclomatic complexity of my code from its control flow graph
  So that I can assess its complexity and plan for appropriate testing and maintenance

  Scenario Outline: getting cyclomatic complexity for a list of functions in a single file 
    Given a code file 'path/to/file'
    When I analyze the file for cyclomatic complexity
    Then I get <cyclomatic_complexity> for the function <function_name>

    Examples:
        | cyclomatic_complexity | function_name           |
        | 1                     | main@7-36@code_file.py  | 
        | 3                     | join@39-53@code_file.py |


  Scenario: getting average cyclomatic complexity for a single file 
    Given a code file 'path/to/file'
    When I analyze the file for average cyclomatic complexity
    Then I get the average cc of '2.0'