import time
from webbrowser import get
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from collections import Counter
import os
import time
from selenium.webdriver.common.keys import Keys
from requests import get
from selenium.webdriver.support.ui import Select

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
    path = '//*[@id="root"]/div[2]/div[2]/div[2]/select/option[' + str(types) + ']'
    # '//*[@id="root"]/div[2]/div[2]/div[2]/select/option[2]'
    context.browser.find_element_by_xpath(path).click()
    time.sleep(2)


@Then('Items should be listed "{byType}"')
def list_type(context, byType):
    for i in range(1, 5):
        time.sleep(1)
        context.browser.execute_script("window.scrollTo(0, window.scrollY + 300)")

    path = '//*[@title="' + byType + '"]'
    assert len(context.browser.find_elements_by_xpath(path)) > 0


@When('searching pokes should be displayed')
def search_pokes(context):
    total_count = get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1').json()["count"]
    pokemons = get('https://pokeapi.co/api/v2/pokemon?offset=0&limit={total}'.format(total=total_count)).json()

    get_pokemons_names = [pokemon["name"] for pokemon in pokemons["results"]]

    menu = Select(context.browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/select'))
    menu_options = [item.get_attribute("value") for item in menu.options]

    for region in menu_options:
        options = Select(context.browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/select'))
        options.select_by_value(region)
        search_box = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[4]/input'))
        )
        search_box.clear()
        for pokemon_name in get_pokemons_names:
            search_box.send_keys(pokemon_name)
            try:
                result = context.browser.find_element_by_class_name("poke__name").text
                assert result.lower() == pokemon_name.lower()
            except NoSuchElementException:
                print("{} is not found in {}".format(pokemon_name, region))
            search_box.clear()