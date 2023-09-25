import pytest

from utils.WebDriver import WebDriver
from utils.constants import BASE_URL


@pytest.fixture
def chrome_driver():
    web_driver = WebDriver(BASE_URL)
    web_driver.set_up_chrome_driver()
    yield web_driver
    web_driver.close_driver()
