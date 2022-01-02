Feature: App Functionality Tests

  @region
  Scenario Outline: Items Counting w/Region
    When Selecting "<region>"
    Then Items should be listed "<minVal>" to "<maxVal>"
    Examples:
      | region | minVal | maxVal |
      | 1  |  1     |151     |
      | 2  |152     |251     |
      | 3  |252     |386     |
      | 4  |387     |494     |
      | 5  |495     |649     |
      | 6  |650     |721     |
      | 7  |722     |809     |
      | 8  |810     |898     |

  @types
  Scenario Outline: Items Counting w/type
    When Selecting of "<types>"
    Then Items should be listed "<byType>"
    Examples:
      | types | byType |
      |2      |grass   |
      |3      |bug     |
      |4      |dark    |
      |5      |dragon  |
      |6      |electric|





