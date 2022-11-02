import pytest
import allure
from tests.acceptance.steps.login_page import LoginPageForm


@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("Test login")
    @allure.description("This is the test of the login flow after registration")
    def test_registration(self, spreadsheet_id, val_range_name, key_range_name):

        login = LoginPageForm(self.driver, spreadsheet_id, val_range_name, key_range_name)
        login.open_page()
        login.enter_login_email()
        login.enter_login_pw()
        login.click_login_button()
        login.login_success()


