from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(2)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
