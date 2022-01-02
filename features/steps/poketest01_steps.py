import time
from behave import *


@Then('logo should be displayed')
def verify_logo(context):
    logo = context.browser.find_element_by_css_selector(".poke__logo")
    assert logo.is_displayed()


@Then('themeSwitch should be displayed')
def verify_switch(context):
    themeSwitch = context.browser.find_element_by_css_selector(".toggle")
    assert themeSwitch.is_displayed()


@Then('github button should be displayed')
def verify_gitButton(context):
    gitButton = context.browser.find_element_by_css_selector(".pokeball__box.github__icon")
    assert gitButton.is_displayed()


@Then('filter items should be displayed')
def verify_filterItems(context):
    for n in range(3):
        path = '//*[@id="root"]/div[2]/div[2]/div['+str(n+1)+']'
        filterItems = context.browser.find_element_by_xpath(path)
        assert filterItems.is_displayed()


@Then('All pokes should be displayed')
def verify_pokes(context):
    """
    for n in range(151):
        path = '//*[@id="root"]/div[2]/div[3]/div/ul/li[' + str(n + 1) + ']'
        pokeCard = context.browser.find_element_by_xpath(path)
        time.sleep(0.5)
        assert pokeCard.is_displayed()
    """
    index = 0
    while True:
        divs = context.browser.find_elements_by_class_name('all__pokemons')
        try:
            assert divs[index].is_displayed()
        except IndexError:
            break  # no more elements, exit the loop
        # context.browser.back()
        index += 1
        # The pokes' visibility test is taking a little longer because the page loads late.
