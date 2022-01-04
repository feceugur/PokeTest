Feature: App Functionality Tests

  @region
  Scenario Outline: Region Filter Test
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
  Scenario Outline: Type filter test
    When Selecting of "<types>"
    Then Items should be listed "<byType>"
    Examples:
      | types | byType  |
      |2      |grass    |
      |3      |bug      |
      |4      |dark     |
      |5      |dragon   |
      |6      |electric |
      |7      |fairy    |
      |8      |fighting |
      |9      |fire     |
      |10     |flying   |
      |11     |ghost    |
      |12     |ground   |
      |13     |ice      |
      |14     |normal   |
      |15     |poison   |
      |16     |poison   |
      |17     |rock     |
      |18     |steel    |
      |19     |water    |

    @search
    Scenario: Search test
      When searching pokes should be displayed





