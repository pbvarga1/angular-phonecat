import time

import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope='session')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def ready(driver):

    def get_browser():
        driver.get('http://app:8000')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is('Google Phone Gallery'), 'Could not load page')
    count = 0
    not_ready = True
    while not_ready:
        try:
            get_browser()
            not_ready = False
        except TimeoutException:
            count += 1
            if count >= 3:
                raise
            time.sleep(3)


@pytest.fixture
def browser(driver: webdriver.Chrome, ready):
    driver.get('http://app:8000')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is('Google Phone Gallery'), 'Could not load page')
    return driver


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.bdd)
