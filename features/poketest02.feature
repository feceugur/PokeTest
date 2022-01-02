Feature: Buttons Functionality Tests

  @funcButton @button
  Scenario: Buttons Functionality
    Given themeSwitch should be functional
    Then gitButton should be functional
    Then filter items should be functional

  @infoButton @pokes
  Scenario: Pokes Functionality
    Then pokes infoButton should be functional