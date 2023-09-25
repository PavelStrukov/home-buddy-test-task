from typing import List, Union

import allure

from pages.ThankYouPage import ThankYouPage
from pages.submit_forms_pages.HVACSubmitForm import HVACSubmitForm
from utils.constants import SetUpProjectSelectItem

HVAC_PAGE_TITLE = 'How Much Does It Cost To Update An HVAC System In {}'
THANK_YOU_PAGE_URL = '/thank-you'
THANK_YOU_PAGE_TITLE = 'Thank you {}, your contractor QA company will call soon!'
NON_EXISTING_ZIP_PAGE_TITLE = 'Unfortunately, I have no matching contractors in your area yet.'


class HVACSubmitFormActions:
    """Class contains actions for tests with HVAC submit form"""

    def __init__(self, driver):
        self.hvac_page = HVACSubmitForm(driver)
        self.thank_you_page = ThankYouPage(driver)

    def wait_page_loaded(self):
        self.hvac_page.wait_page_loaded()

    @allure.step('Check page title')
    def check_page_title(self, location: str = None):
        actual_title = self.hvac_page.get_page_title()
        failure_message = 'Unexpected page title for Main Page'
        if location is None:
            expected_title = HVAC_PAGE_TITLE.replace('{}', '')
            assert expected_title in actual_title, failure_message
        else:
            expected_title = HVAC_PAGE_TITLE.format(location)
            assert expected_title == actual_title, failure_message

    @allure.step('Check zip code input with value {zip_code}')
    def input_zip_code(self, zip_code: str, error_message: str = None):
        if error_message is None:
            self.hvac_page.check_valid_zip_code_input(zip_code)
        else:
            self.hvac_page.check_invalid_zip_code_input(zip_code, error_message)

    @allure.step('Click "Get estimate" button')
    def click_get_estimate_button(self):
        self.hvac_page.click_submit_button()
        self.wait_page_loaded()

    @allure.step('Select application options: {expected_options}')
    def select_application_options(self, expected_options: Union[List[SetUpProjectSelectItem], SetUpProjectSelectItem]):
        if isinstance(expected_options, SetUpProjectSelectItem):
            expected_options = [expected_options]

        option_ids = [option.automation_id for option in expected_options]

        if any([option.value in ['Yes', 'No'] for option in expected_options]):
            self.hvac_page.select_div_options(option_ids)
        else:
            self.hvac_page.select_options(option_ids)

    @allure.step('Check square feet input with value {square_feet}')
    def input_square_feet(self, square_feet: int, not_sure: bool = False, error_message: str = None):
        if not_sure:
            self.hvac_page.click_not_sure()
        else:
            if error_message is None:
                self.hvac_page.check_valid_square_feet_input(square_feet)
            else:
                self.hvac_page.check_invalid_square_feet_input(square_feet, error_message)

    @allure.step('Check full name and email inputs with values {full_name}, {email}')
    def input_full_name_and_email(self, full_name: str, email: str, full_name_error: str = None,
                                  email_error: str = None):
        if full_name_error is None:
            self.hvac_page.check_valid_full_name_input(full_name)
        else:
            self.hvac_page.check_invalid_full_name_input(full_name, full_name_error)

        if email_error is None:
            self.hvac_page.check_valid_email_input(email)
        else:
            self.hvac_page.check_invalid_email_input(email, email_error)

    @allure.step('Check phone number input with value {phone_number}')
    def input_phone_number(self, phone_number: str, expected_error: str = None):
        if expected_error is None:
            self.hvac_page.check_valid_phone_number_input(phone_number)
        else:
            self.hvac_page.check_invalid_phone_number_input(phone_number, expected_error)

    @allure.step('Click "Next" button')
    def click_next_button(self):
        self.hvac_page.click_next_button()
        self.hvac_page.wait_page_loaded()

    @allure.step('Check "Thank you" page')
    def check_thank_you_page(self, user_name: str):
        self.thank_you_page.wait_page_loaded()
        self.thank_you_page.check_page_url(THANK_YOU_PAGE_URL)
        actual_page_title = self.thank_you_page.get_page_title()
        assert actual_page_title == THANK_YOU_PAGE_TITLE.format(user_name), 'Unexpected "Thank you" page title'

    @allure.step('Check non existing zip code form opened')
    def check_non_existing_zip_form_opened(self):
        actual_page_title = self.hvac_page.non_existing_zip_section.get_page_title()
        assert actual_page_title == NON_EXISTING_ZIP_PAGE_TITLE, 'Unexpected "Thank you" page title'

        self.hvac_page.non_existing_zip_section.check_email_input_is_visible()
        self.hvac_page.non_existing_zip_section.check_submit_button_is_visible()

    @allure.step('Check "Try another zip code" button')
    def check_try_another_zip_code_button(self):
        self.hvac_page.non_existing_zip_section.click_try_another_zip_code_button()

        self.wait_page_loaded()
        self.check_page_title()
