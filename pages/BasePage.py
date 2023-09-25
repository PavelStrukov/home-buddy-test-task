import logging

from pages.PageObject import PageObject

logger = logging.getLogger(__name__)


class BasePage(PageObject):
    """Class represents common elements and methods for all pages"""
    HEADER_LOGO = "//div[contains(@class, 'logo')]"
    LOADER = "//span[contains(@class, 'animation_spin')]"
    PAGE_TITLE = "//h1[@class='header__title']"
    SUBMIT_BUTTON = "//button[@data-autotest-button-submit-0]"

    def wait_header_logo_appeared(self):
        logger.info('Wait header logo appeared')
        self.wait_appear(self.HEADER_LOGO)

    def wait_page_loaded(self):
        logger.info('Wait page loaded')
        self.wait_disappear(self.LOADER)
        self.wait_header_logo_appeared()

    def get_page_title(self) -> str:
        logger.info('Get page title')
        return self.find_element(self.PAGE_TITLE).text

    def click_submit_button(self) -> None:
        logger.info('Click "Submit" button')
        self.click(self.SUBMIT_BUTTON)

    def check_page_url(self, expected_url: str):
        logger.info('Check page url')
        actual_url = self.driver.driver.current_url
        assert actual_url == f'{self.driver.base_url}{expected_url}', 'Unexpected page url'
