import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from tests.acceptance.locators.login_register_page import LogInLocators
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.utils.google_sheet_data.gsheet_api import GsheetData


class LoginPageForm(BasePage, GsheetData):

    def __init__(self, driver, spreadsheet_id, val_range_name, key_range_name):
        self.driver = driver
        super().__init__(spreadsheet_id=spreadsheet_id, val_range_name=val_range_name, key_range_name=key_range_name)

    @property
    def get_data(self):
        data = GsheetData(self.spreadsheet_id, self.val_range_name, self.key_range_name).get_gsheet_data()
        return data

    @property
    def url(self):
        return super(LoginPageForm, self).url + '?controller=authentication&back=my-account'

    @allure.step("Open the website")
    def open_page(self):
        self.driver.get(self.url)

    @allure.step("Enter the email")
    def enter_login_email(self):
        data = self.get_data
        value = data.get('acc_email')
        self.driver.find_element(*LogInLocators.LOGIN_EMAIL).send_keys(value)

    @allure.step("Enter the password")
    def enter_login_pw(self):
        data = self.get_data
        value = data.get('password')
        self.driver.find_element(*LogInLocators.LOGIN_PW).send_keys(value)

    @allure.step("click the login button")
    def click_login_button(self):
        self.driver.find_element(*LogInLocators.LOGIN_BUTTON).click()

    @allure.step("check if the user successfully log in")
    def login_success(self):
        expected_url = 'http://automationpractice.com/index.php?controller=my-account'
        assert self.driver.current_url == expected_url
        







