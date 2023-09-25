from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.WebDriver import WebDriver


class PageObject:
    """Class wrapper for all objects and pages"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_appear(self, locator: str, timeout: int = None) -> None:
        wait = WebDriverWait(self.driver.driver, timeout or self.driver.current_implicit_wait)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)),
                   message=f'Element: {locator} did not appear as expected')

    def wait_disappear(self, locator: str, timeout: int = None) -> None:
        wait = WebDriverWait(self.driver.driver, timeout or self.driver.current_implicit_wait)
        wait.until(EC.invisibility_of_element_located((By.XPATH, locator)),
                   message=f'Element: {locator} did not disappear as expected')

    def get_element(self, locator: str) -> WebElement:
        return self.driver.driver.find_element(By.XPATH, locator)

    def find_element(self, locator: str, timeout: int = None) -> WebElement:
        self.wait_appear(locator, timeout)
        return self.get_element(locator)

    def get_nested_element(self, parent_locator: str, target_element_locator: str) -> WebElement:
        return self.get_element(parent_locator).find_element(By.XPATH, target_element_locator)

    def input_value(self, object_locator: str, input_value: Union[str, int, float]) -> None:
        self.find_element(object_locator).send_keys(input_value)

    def click(self, locator: str, timeout: int = None) -> None:
        wait = WebDriverWait(self.driver.driver, timeout or self.driver.current_implicit_wait)
        elem = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        elem.click()
