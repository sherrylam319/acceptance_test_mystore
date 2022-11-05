import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.utils.google_sheet_data.gsheet_api import GsheetData
from tests.acceptance.locators.login_register_page import PersonalInfoLocators


class PersonalPage(BasePage, GsheetData):

    def __init__(self, driver, spreadsheet_id, val_range_name, key_range_name):
        self.driver = driver
        super().__init__(spreadsheet_id=spreadsheet_id, val_range_name=val_range_name, key_range_name=key_range_name)

    @property
    def get_data(self):
        data = GsheetData(self.spreadsheet_id, self.val_range_name, self.key_range_name).get_gsheet_data()
        return data

    @property
    def url(self):
        return super(PersonalPage, self).url + '?controller=authentication&back=my-account'

    @allure.step("Open the website")
    def open_page(self):
        self.driver.get(self.url)

    @allure.step("Click the personal info button")
    def click_personal_info_button(self):
        self.driver.find_element(*PersonalInfoLocators.PERSONAL_INFO_BUTTON).click()


    def check_social_title(self):
        data = self.get_data
        value = data.get('title')

        if value == "Mr":
            element = self.driver.find_element(*PersonalInfoLocators.RADIO_MR_PI)
            assert element.is_selected()
        elif value == "Mrs":
            element = self.driver.find_element(*PersonalInfoLocators.RADIO_MRS_PI)
            assert element.is_selected()


    def check_first_name(self):
        data = self.get_data
        value = data.get('first_name')

        element = self.driver.find_element(By.XPATH, f"//input[@id='firstname' and @value='{value}']")
        assert element.is_displayed()


    def check_last_name(self):
        data = self.get_data
        value = data.get('last_name')

        assert self.driver.find_element(By.XPATH, f"//input[@id='lastname' and @value='{value}']").is_displayed()


    def check_email(self):
        data = self.get_data
        value = data.get('acc_email')

        assert self.driver.find_element(By.XPATH, f"//input[@id='email' and @value='{value}']").is_displayed()


    def check_birth_day(self):
        data = self.get_data
        value = data.get('day')

        assert self.driver.find_element(By.XPATH, f"//option[@value='{value}' and @selected='selected']").is_displayed()


    def check_birth_month(self):
        data = self.get_data
        value = data.get('month')
        assert self.driver.find_element(By.XPATH, f"//option[contains(text(), '{value}') and @selected='selected']").is_displayed()


    def check_birth_year(self):
        data = self.get_data
        value = data.get('year')
        assert self.driver.find_element(By.XPATH, f"//option[@value='{value}' and @selected='selected']").is_displayed()





