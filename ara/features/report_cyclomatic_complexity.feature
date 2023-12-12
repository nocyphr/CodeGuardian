Feature: Calculate Cyclomatic Complexity from Control Flow Graph

  As a software developer
  I want to calculate the cyclomatic complexity of my code from its control flow graph
  So that I can assess its complexity and plan for appropriate testing and maintenance

  Scenario: Inferring Edge, Node, and Component Counts from Control Flow Graph
    Given a textual control flow graph 'path/to/file' of a single code file
    When I send the graph to an agent
    Then the AI agent infers the number of edges, nodes, and connected components

  Scenario: Calculating Cyclomatic Complexity with Inferred Values
    Given inferred values of edges, nodes, and connected components from the AI agent
    When I execute the cyclomatic complexity calculation command
    Then the AI agent calculates and returns the cyclomatic complexity using the formula CC = E - N + 2P

  Scenario: Handling Incomplete or Incorrect Control Flow Graph
    Given an incomplete or incorrectly structured control flow graph
    When I feed the graph to the AI agent
    Then the AI agent indicates the errors or missing elements in the graph

  Scenario: Updating Cyclomatic Complexity After Graph Modification
    Given an existing control flow graph with known cyclomatic complexity
    When I modify the graph by adding or removing edges or nodes
    Then the AI agent recalculates
