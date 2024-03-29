import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach


@pytest.fixture( autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://www.neoflex.ru/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.driver.set_window_position(0, 0)
    browser.config.driver.implicitly_wait(4)

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()