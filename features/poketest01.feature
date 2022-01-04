Feature: Visibility Tests

  @smoke @testt
  Scenario: Logo Verification
    Then logo should be displayed

  @button @testt
  Scenario: Buttons Visibility
    Then themeSwitch should be displayed
    Then github button should be displayed
    Then filter items should be displayed

  @pokes @testt
  Scenario: Poke Visibility
    Then All pokes should be displayed
