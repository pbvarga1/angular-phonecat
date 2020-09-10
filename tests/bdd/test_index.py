from __future__ import annotations

from time import sleep

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
    scenarios,
)
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

scenarios('index.feature')


@given('the window')
def the_window(browser: webdriver.Chrome):
    """The window is open."""
    return browser


@when('the user sorts alphabetically')
def sort_alphabetically(browser: webdriver.Chrome):
    select = Select(browser.find_element_by_id('sort-by'))
    select.select_by_value('name')


@when(parsers.parse('the user searches "{text}"'))
def search_by_text(browser: webdriver.Chrome, text: str):
    input_element: WebElement = browser.find_element_by_id("phone-search")
    input_element.send_keys(text)
    sleep(1)


@then(parsers.parse('the first item is "{name}"'))
def the_text_the_is(browser: webdriver.Chrome, name: str):
    """The text is "line"."""
    elements: list[WebElement] = browser.find_elements_by_class_name(
        "phone-list-item"
    )
    assert len(elements) > 2
    element = elements[0]
    element = element.find_element_by_class_name("phone-link")
    assert element.text == name
