import pytest

from tests.BaseTest import BaseTest
from utils.common_functions import generate_valid_email, generate_valid_name
from utils.constants import ProjectTypes, InvolvedEquipment, HVACResource, EquipmentAge, PropertyType, AuthorizedOrOwner

HVAC_URL_SUFFIX = '/hvac'
VALID_ZIP_CODE = 10001
VALID_SQUARE_FEET = 150
VALID_PHONE_NUMBER = '2345678901'
HVAC_SETUP_FORM_OPTIONS = [
    ProjectTypes.REPLACEMENT.value,
    [InvolvedEquipment.AIR_COND.value, InvolvedEquipment.BOILER.value],
    HVACResource.GAS.value,
    EquipmentAge.FROM_5_TO_10.value,
    PropertyType.DETACHED.value
]

INVALID_ZIP_DATA = [
    ('', 'A ZIP Code is required'),
    (1, 'The ZIP Code must be 5 digits with no spaces'),
    (1000, 'The ZIP Code must be 5 digits with no spaces'),
    (100001, 'The ZIP Code must be 5 digits with no spaces'),
    ('asdfg', 'The ZIP Code must be 5 digits with no spaces'),
    ('10 001', 'The ZIP Code must be 5 digits with no spaces')
]
NON_EXISTING_ZIP_CODE = '00000'


class TestHVACApplication(BaseTest):

    @pytest.fixture(autouse=True)
    def open_hvac_page(self, chrome_driver):
        self.open_page(chrome_driver, HVAC_URL_SUFFIX)

    def test_check_successful_submit_hvac_application(self):
        full_name, email = generate_valid_name(), generate_valid_email()
        self.hvac_submit_actions.input_zip_code(VALID_ZIP_CODE)
        self.hvac_submit_actions.click_get_estimate_button()

        for hvac_options in HVAC_SETUP_FORM_OPTIONS:
            self.hvac_submit_actions.select_application_options(hvac_options)
            self.hvac_submit_actions.click_next_button()

        self.hvac_submit_actions.input_square_feet(VALID_SQUARE_FEET)
        self.hvac_submit_actions.click_next_button()

        self.hvac_submit_actions.select_application_options(AuthorizedOrOwner.YES.value)
        self.hvac_submit_actions.click_next_button()

        self.hvac_submit_actions.input_full_name_and_email(full_name, email)
        self.hvac_submit_actions.input_phone_number(VALID_PHONE_NUMBER)

        first_name = full_name.split()[0]
        self.hvac_submit_actions.check_thank_you_page(first_name)

    @pytest.mark.parametrize('zip_value, expected_message', INVALID_ZIP_DATA)
    def test_invalid_zip_code_value(self, zip_value, expected_message):
        self.hvac_submit_actions.input_zip_code(zip_value, expected_message)

    def test_non_existing_zip_code(self):
        self.hvac_submit_actions.input_zip_code(NON_EXISTING_ZIP_CODE)
        self.hvac_submit_actions.click_get_estimate_button()
        self.hvac_submit_actions.check_non_existing_zip_form_opened()
        self.hvac_submit_actions.check_try_another_zip_code_button()
