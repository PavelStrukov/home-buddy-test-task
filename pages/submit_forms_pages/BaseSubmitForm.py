import logging
from typing import Union

from pages.BasePage import BasePage

logger = logging.getLogger(__name__)


class NonExistingZip(BasePage):
    """Class represents elements of non existing zip page object in Submit form page"""
    def __init__(self, driver, parent):
        self.parent = parent
        super().__init__(driver)

    PAGE_TITLE = "//h4"
    SUBMIT_BUTTON = "//button[@data-autotest-button-submit-submit]"
    TRY_ANOTHER_ZIP_CODE = "//button[@data-autotest-button-try-another-zip]"

    def check_email_input_is_visible(self) -> None:
        logger.info('Check email input is visible in non existing zip page object')
        failure_message = 'Unexpected input email state. Expected it is visible'
        assert self.find_element(self.parent.EMAIL_INPUT).is_displayed(), failure_message

    def check_submit_button_is_visible(self) -> None:
        logger.info('Check submit is visible in non existing zip page object')
        failure_message = 'Unexpected submit button state. Expected it is visible'
        assert self.find_element(self.SUBMIT_BUTTON).is_displayed(), failure_message

    def click_try_another_zip_code_button(self) -> None:
        logger.info('Click "try another zip code" button in non existing zip page object')
        self.click(self.TRY_ANOTHER_ZIP_CODE)


class BaseSubmitForm(BasePage):
    """Class represents common elements of submit form"""
    ZIP_INPUT = "//input[@data-autotest-input-0]"
    CORRECT_ZIP_ICON = "./div[@class='rightIcon']"
    INCORRECT_ZIP_MESSAGE = "//div[@class='zip--caption']"
    SELECT_OPTION_TEMPLATE = "//li[.//input[@{}]]"
    SELECT_OPTION_DIV_TEMPLATE = "//div[.//input[@{}]]/label"
    NEXT_BUTTON = "//button[@data-autotest-button-submit-next]"
    SQUARE_FEET_INPUT = "//input[@data-autotest-input-squarefeet-tel]"
    INCORRECT_INPUT_MESSAGE_TEMPLATE = ("//div[.{} and contains(@class, 'customInput_primary')]"
                                        "//div[@class='customInput__message']")
    NOT_SURE = "//input[@data-autotest-checkbox-notsure-]"
    FULL_NAME_INPUT = "//input[@data-autotest-input-fullname-text]"
    EMAIL_INPUT = "//input[@data-autotest-input-email-email]"
    PHONE_NUMBER_INPUT = "//input[@data-autotest-input-phonenumber-tel]"
    SUBMIT_MY_REQUEST = "//button[@data-autotest-button-submit-submit-my-request]"

    @property
    def non_existing_zip_section(self) -> NonExistingZip:
        return NonExistingZip(self.driver, self)

    def check_valid_zip_code_input(self, zip_code: str) -> None:
        logger.info(f'Check zip code input with valid value: {zip_code}')
        self.input_value(self.ZIP_INPUT, zip_code)
        message = 'Correct zip icon is not displayed as expected'
        assert self.get_nested_element(f'{self.ZIP_INPUT}/..', self.CORRECT_ZIP_ICON).is_displayed(), message

    def check_invalid_zip_code_input(self, zip_code: str, error_message: str) -> None:
        logger.info(f'Check zip code input with invalid value: {zip_code}')
        self.input_value(self.ZIP_INPUT, zip_code)
        self.click_submit_button()
        actual_message = self.find_element(self.INCORRECT_ZIP_MESSAGE).text
        assert actual_message == error_message, 'Unexpected error message for invalid zip code'

    def select_options(self, option_ids: list):
        logger.info(f'Select options with ids: {option_ids}')
        for option_id in option_ids:
            self.click(self.SELECT_OPTION_TEMPLATE.format(option_id))

    def select_div_options(self, option_ids: list):
        logger.info(f'Select options with ids: {option_ids}')
        for option_id in option_ids:
            self.click(self.SELECT_OPTION_DIV_TEMPLATE.format(option_id))

    def click_next_button(self):
        logger.info('Click next button')
        self.click(self.NEXT_BUTTON)

    def check_valid_square_feet_input(self, square_feet: Union[int, float]):
        logger.info(f'Check square feet input with valid value: {square_feet}')
        self.input_value(self.SQUARE_FEET_INPUT, square_feet)
        failure_message = 'Unexpected square feet error message found, expected to be absent'
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.SQUARE_FEET_INPUT)
        assert not self.get_element(error_msg_locator).text, failure_message

    def check_invalid_square_feet_input(self, square_feet: Union[int, float], expected_message: str):
        logger.info(f'Check square feet input with invalid value: {square_feet}')
        self.input_value(self.SQUARE_FEET_INPUT, square_feet)
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.SQUARE_FEET_INPUT)
        actual_message = self.get_element(error_msg_locator).text
        assert actual_message == expected_message, 'Unexpected square feet error message'

    def click_not_sure(self):
        logger.info('Click "Not sure" checkbox')
        self.click(self.NOT_SURE)

    def check_valid_full_name_input(self, full_name: str):
        logger.info(f'Check full name input with valid value: {full_name}')
        self.input_value(self.FULL_NAME_INPUT, full_name)
        self.click_next_button()
        failure_message = 'Unexpected full name error message found, expected to be absent'
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.FULL_NAME_INPUT)
        assert not self.get_element(error_msg_locator).text, failure_message

    def check_invalid_full_name_input(self, full_name: str, expected_message: str):
        logger.info(f'Check full name input with invalid value: {full_name}')
        self.input_value(self.FULL_NAME_INPUT, full_name)
        self.click_next_button()
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.FULL_NAME_INPUT)
        actual_message = self.get_element(error_msg_locator).text
        assert actual_message == expected_message, 'Unexpected full name error message'

    def check_valid_email_input(self, email: str):
        logger.info(f'Check email input with valid value: {email}')
        self.input_value(self.EMAIL_INPUT, email)
        self.click_next_button()
        failure_message = 'Unexpected email error message found, expected to be absent'
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.EMAIL_INPUT)
        assert not self.get_element(error_msg_locator).text, failure_message

    def check_invalid_email_input(self, email: str, expected_message: str):
        logger.info(f'Check email input with invalid value: {email}')
        self.input_value(self.EMAIL_INPUT, email)
        self.click_next_button()
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.EMAIL_INPUT)
        actual_message = self.get_element(error_msg_locator).text
        assert actual_message == expected_message, 'Unexpected email error message'

    def check_valid_phone_number_input(self, phone_number: str):
        logger.info(f'Check phone number input with valid value: {phone_number}')
        self.input_value(self.PHONE_NUMBER_INPUT, phone_number)
        self.click_submit_my_request()
        failure_message = 'Unexpected phone number error message found, expected to be absent'
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.PHONE_NUMBER_INPUT)
        assert not self.get_element(error_msg_locator).text, failure_message

    def check_invalid_phone_number_input(self, phone_number: str, expected_message: str):
        logger.info(f'Check phone number input with invalid value: {phone_number}')
        self.input_value(self.PHONE_NUMBER_INPUT, phone_number)
        self.click_submit_my_request()
        error_msg_locator = self.INCORRECT_INPUT_MESSAGE_TEMPLATE.format(self.PHONE_NUMBER_INPUT)
        actual_message = self.get_element(error_msg_locator).text
        assert actual_message == expected_message, 'Unexpected phone number error message'

    def click_submit_my_request(self):
        logger.info('Click "Submit my request" button')
        self.click(self.SUBMIT_MY_REQUEST)
