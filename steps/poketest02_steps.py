import time

from behave import *


@Given('themeSwitch should be functional')
def func_button(context):
    themeData = context.browser.find_element_by_css_selector("[data-theme]")
    # print(repr(themeData.text))
    context.browser.find_element_by_css_selector(".toggle").click()
    # time.sleep(1)
    assert themeData.get_attribute('data-theme') == "dark"
    context.browser.find_element_by_css_selector(".toggle").click()


# LIGHT DARK GECISINE BAK TEKRARDAN

@Then('gitButton should be functional')
def func_gitButton(context):
    window_before = context.browser.window_handles[0]
    context.browser.find_element_by_css_selector('.pokeball__box.github__icon').click()
    window_after = context.browser.window_handles[1]
    context.browser.switch_to_window(window_after)
    assert context.browser.title == 'GitHub - s1varam/pokedex: ' \
                                    'A simple Pokémon catalogue, built with React, Material-UI and PokéAPI.'
    context.browser.switch_to_window(window_before)


@Then('filter items should be functional')
def func_filterButton(context):
    index = 0
    while True:
        divs = context.browser.find_elements_by_class_name('filter__items')
        try:
            divs[index].click()
            assert context.failed is False
        except IndexError:
            break  # no more elements, exit the loop
        index += 1
        time.sleep(2)


@Then('pokes infoButton should be functional')
def func_infoButton(context):
    index = 0
    while True:
        divs = context.browser.find_elements_by_class_name('info__icon')
        try:
            divs[index].click()
        except IndexError:
            break  # no more elements, exit the loop
        context.browser.back()
        index += 1

# BROWSER BACK CALISMIYOR CUNKU SAYFA AYNI ISIMLE ACILIYOR
# CREATE ISSUE FOR THIS
