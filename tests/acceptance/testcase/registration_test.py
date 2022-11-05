import pytest
import allure
from tests.acceptance.steps.register_page import RegisterPageForm
from tests.acceptance.steps.personal_info_page import PersonalPage

@pytest.mark.usefixtures("setup")
class TestRegistration:

    @allure.title("Test Registration")
    @allure.description("This is the test of the registration flow")
    def test_registration(self, spreadsheet_id, val_range_name, key_range_name):

        registration = RegisterPageForm(self.driver, spreadsheet_id, val_range_name, key_range_name)

        registration.open_page()
        registration.create_acc_email()
        registration.create_acc_button()
        registration.wait_after_acc_b()
        registration.select_title()
        registration.set_first_name()
        registration.set_last_name()
        registration.set_password()
        registration.birthday()
        registration.address_1()
        registration.address_2()
        registration.set_city()
        registration.set_state()
        registration.set_zip_code()
        registration.set_country()
        registration.set_mobile_phone()
        registration.set_alias()
        registration.click_register_button()
        registration.registration_success()

    @allure.title("Social Title Test")
    @allure.description("Check if the social title is the title checked in the registration page")
    def test_social_title(self, spreadsheet_id, val_range_name, key_range_name):

        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.click_personal_info_button()
        personal_info.check_social_title()

    @allure.title("First Name Test")
    @allure.description("Check if the first name is the same as the one entered on registration page")
    def test_first_name(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_first_name()

    @allure.title("Last Name Test")
    @allure.description("Check if the last name is the same as the one entered on registration page")
    def test_last_name(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_last_name()

    @allure.title("Email Test")
    @allure.description("Check if the email is the same as the one entered on registration page")
    def test_email(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_email()

    @allure.title("Birth Day Test")
    @allure.description("Check if the day of birth is the same as the one entered on registration page")
    def test_birth_day(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_birth_day()

    @allure.title("Birth Month Test")
    @allure.description("Check if the month of birth is the same as the one entered on registration page")
    def test_birth_month(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_birth_month()

    @allure.title("Birth Year Test")
    @allure.description("Check if the year of birth is the same as the one entered on registration page")
    def test_birth_year(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_birth_year()






#In the terminal, run:
#1. pytest the/full/path/of/your/directory/My_Store_git/MyStore_acceptance_test/tests/acceptance/testcase/registration_test.py --alluredir=allure-report/
#2. allure serve allure-report/
