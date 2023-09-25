from selenium import webdriver

from utils.constants import DEFAULT_WAIT


class WebDriver:
    def __init__(self, base_url, implicit_wait=DEFAULT_WAIT):
        self.driver = None
        self.base_url = base_url
        self.current_implicit_wait = implicit_wait

    def set_up_chrome_driver(self):
        self.driver = webdriver.Chrome()

    def open_base_url(self):
        self.driver.get(self.base_url)

    def open_page(self, page_url_path):
        self.driver.get(f'{self.base_url}{page_url_path}')

    def close_driver(self):
        self.driver.close()
