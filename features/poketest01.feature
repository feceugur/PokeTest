Feature: Visibility Tests

  @smoke
  Scenario: Logo Verification
    Then logo should be displayed

  @button
  Scenario: Buttons Visibility
    Then themeSwitch should be displayed
    Then github button should be displayed
    Then filter items should be displayed

  @pokes
  Scenario: Poke Visibility
    Then All pokes should be displayed
