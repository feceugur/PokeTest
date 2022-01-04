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


@When('searching pokes should be displayed for "{region}" from "{minVal}')
def search_pokes(context, region, minVal):
    path = '//*[@id="root"]/div[2]/div[2]/div[1]/select/option[' + str(region) + ']'
    context.browser.find_element_by_xpath(path).click()
    time.sleep(3)

    total_count = get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1').json()["count"]
    api_path = 'https://pokeapi.co/api/v2/pokemon?offset=' + str(minVal) + '&limit={total}'
    pokemons = get(api_path.format(total=total_count)).json()

    get_pokemons_names = [pokemon["name"] for pokemon in pokemons["results"]]

    search_box = context.browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[4]/input')
    search_box.clear()
    for pokemon_name in get_pokemons_names:
        search_box.send_keys(pokemon_name)
        search_box.clear()
        time.sleep(1)
        try:
            result = context.browser.find_element_by_class_name("poke__name").text
            try:
                assert result.lower() == pokemon_name.lower()
            except AssertionError:
                print("Pokemon name is not correct {}".format(result))
        except NoSuchElementException:
            nopoke = context.browser.find_element_by_class_name('no__data noselect').text
            if nopoke is "No such Pokémon in this region :/":
                print("No such Pokémon in this region :/")
