import time

from behave import *
import time


@When('Selecting "{region}"')
def select_region(context, region):
    path = '//*[@id="root"]/div[2]/div[2]/div[1]/select/option[' + str(region) + ']'
    context.browser.find_element_by_xpath(path).click()
    time.sleep(5)


@Then('Items should be listed "{minVal}" to "{maxVal}"')
def list_vals(context, minVal, maxVal):
    for i in range(1, 55):
        time.sleep(1)
        context.browser.execute_script("window.scrollTo(0, window.scrollY + 300)")

    poke_number = context.browser.find_elements_by_class_name("poke__number")
    poke_list = []
    for i in poke_number:
        poke_list.append(int(i.text.replace("#", "")))

    check_list = [i for i in range(int(minVal), int(maxVal) + 1)]
    check = set(check_list) ^ set(poke_list)
    assert len(check) == 0


@When('Selecting of "{types}"')
def select_type(context, types):
    path = '//*[@id="root"]/div[2]/div[2]/div[2]/select/option[' + types + ']'
    context.browser.find_element_by_xpath(path).click()
    time.sleep(2)


@Then('Items should be listed "{byType}"')
def list_type(context, byType):

    path = '//*[@title="'+byType+'"]'
    assert len(context.browser.find_elements_by_xpath(path)) > 0
