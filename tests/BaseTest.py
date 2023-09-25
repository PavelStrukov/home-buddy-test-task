import pytest

from actions.HVACSubmitFormActions import HVACSubmitFormActions


class BaseTest:

    @classmethod
    def init_actions(cls, driver):
        cls.hvac_submit_actions = HVACSubmitFormActions(driver)

    def open_page(self, chrome_driver, page_suffix: str = None):
        self.init_actions(chrome_driver)
        if page_suffix is None:
            chrome_driver.open_base_url()
        else:
            chrome_driver.open_page(page_suffix)

        self.hvac_submit_actions.wait_page_loaded()
        self.hvac_submit_actions.check_page_title()

    @pytest.fixture
    def open_home_page(self, chrome_driver):
        self.open_page(chrome_driver)
