import pytest
import allure
from tests.acceptance.steps.register_page import RegisterPageForm
from tests.acceptance.steps.personal_info_page import PersonalPage

@pytest.mark.usefixtures("setup")
class TestRegistration:

    @allure.title("Test registration")
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


    def test_social_title(self, spreadsheet_id, val_range_name, key_range_name):

        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.click_personal_info_button()
        personal_info.check_social_title()

    def test_first_name(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_first_name()

    def test_last_name(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_last_name()

    def test_email(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_email()

    def test_birth_day(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_birth_day()

    def test_birth_month(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_birth_month()

    def test_birth_year(self, spreadsheet_id, val_range_name, key_range_name):
        personal_info = PersonalPage(self.driver, spreadsheet_id, val_range_name, key_range_name)
        personal_info.check_birth_year()










#pytest --collect-only tests/acceptance/steps/registration_test.py --alluredir=allure-report/

#pytest /Users/admin/Documents/Sherry/MyStore/tests/acceptance/steps/registration_test.py --alluredir=allure-report/

#pytest /Users/admin/Documents/Sherry/MyStore/tests/acceptance/steps/registration_test.py --alluredir=allure-report/


#pytest /Users/sherrylam/Documents/software_testing/browser_auto/MyStore/tests/acceptance/steps/registration_test.py --alluredir=allure-report/
