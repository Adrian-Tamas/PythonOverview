Feature: Addition Feature

  Scenario: Add Two Numbers
    Given I have the number 3
    And I have the number 4
    When I add the numbers together
    Then the result should be 7

  Scenario Outline: Add Two Numbers with example table
    Given I have the number <num1>
    And I have the number <num2>
    When I add the numbers together
    Then the result should be <expected_result>

  Examples:
      | num1 | num2 | expected_result |
      | 3    | 4    | 7               |
      | 2    | 5    | 7               |
      | 0    | 0    | 0               |
