import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture
def driver():
    # По заданию используется браузер Mozilla Firefox
    browser = webdriver.Firefox()
    browser.set_window_size(1920, 1080)
    browser.get(Urls.BASE_URL)

    yield browser

    browser.quit()
