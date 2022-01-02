import time

from selenium import webdriver
import os
import time


def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    context.browser = webdriver.Chrome(os.getcwd() + "/chromedriver",
                                       chrome_options=chrome_options)

    context.browser.get('https://pokedex-react-mui.netlify.app/')
    time.sleep(3)


def after_all(context):
    context.browser.quit()
