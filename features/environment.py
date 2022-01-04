from selenium import webdriver


def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-dev-shm-usage')

    chrome = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=chrome_options)
    firefox = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=firefox_options)

    browsers = [chrome, firefox]
    for browser in browsers:
        context.browser = browser
        context.browser.get('https://pokedex-react-mui.netlify.app/')


def after_all(context):
    context.browser.quit()
