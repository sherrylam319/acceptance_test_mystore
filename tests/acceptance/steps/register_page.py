import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from tests.acceptance.locators.login_register_page import RegisterPageLocators
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.utils.google_sheet_data.gsheet_api import GsheetData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from tests.acceptance.utils.path import *



class RegisterPageForm(BasePage, GsheetData):

    def __init__(self, driver, spreadsheet_id, val_range_name, key_range_name):
        self.driver = driver
        super().__init__(spreadsheet_id=spreadsheet_id, val_range_name=val_range_name, key_range_name=key_range_name)


    @property
    def get_data(self):
        data = GsheetData(self.spreadsheet_id, self.val_range_name, self.key_range_name).get_gsheet_data()
        return data

    @property
    def url(self):
        return super(RegisterPageForm, self).url + '?controller=authentication&back=my-account'

    @allure.step("Open the website")
    def open_page(self):
        self.driver.get(self.url)

    @allure.step("Enter an email for creating account")
    def create_acc_email(self):
        data = self.get_data
        value = data.get('acc_email')
        self.driver.find_element(*RegisterPageLocators.CREATE_ACC_EMAIL).click()
        self.driver.find_element(*RegisterPageLocators.CREATE_ACC_EMAIL).send_keys(value)

    @allure.step("click the create an account button")
    def create_acc_button(self):
        self.driver.find_element(*RegisterPageLocators.CREATE_ACC_BUTTON).click()

    @allure.step("wait for the next page to load")
    def wait_after_acc_b(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.RADIO_MR)
        )

    @allure.step("Selecting a title")
    def select_title(self):
        data = self.get_data
        value = data.get('title')

        if value == 'Mr':
            self.driver.find_element(*RegisterPageLocators.RADIO_MR).click()
        elif value == 'Mrs':
            self.driver.find_element(*RegisterPageLocators.RADIO_MRS).click()
        else:
            raise Exception("No such option, please enter a valid title")

    @allure.step("Entering first name")
    def set_first_name(self):
        data = self.get_data
        value = data.get('first_name')
        self.driver.find_element(*RegisterPageLocators.SET_FIRST_NAME).send_keys(value)

    @allure.step("Entering last name")
    def set_last_name(self):
        data = self.get_data
        value = data.get('last_name')
        self.driver.find_element(*RegisterPageLocators.SET_LAST_NAME).send_keys(value)

    @allure.step("Entering an email address")
    def set_email_address(self):
        data = self.get_data
        value = data.get('email')
        self.driver.find_element(*RegisterPageLocators.SET_EMAIL).send_keys(value)

    @allure.step("Enter password")
    def set_password(self):
        data = self.get_data
        value = data.get('password')
        self.driver.find_element(*RegisterPageLocators.SET_PASSWORD).send_keys(value)

    @allure.step("Click the dropdown and choose a birthday'")
    def birthday(self):
        data = self.get_data
        day = data.get('day')
        month = data.get('month')
        year = data.get('year')
        self.driver.find_element(*RegisterPageLocators.DAY_OF_BIRTH).click()
        self.driver.find_element(By.XPATH, f"//option[@value='{day}']").click()

        self.driver.find_element(*RegisterPageLocators.MONTH_OF_BIRTH).click()
        self.driver.find_element(By.XPATH, f"//option[contains(text(), '{month}')]").click()

        self.driver.find_element(*RegisterPageLocators.YEAR_OF_BIRTH).click()
        self.driver.find_element(By.XPATH, f"//option[@value='{year}']").click()

    @allure.step("Enter address in the address box 1")
    def address_1(self):
        data = self.get_data
        value = data.get('address_1')
        self.driver.find_element(*RegisterPageLocators.ADDRESS_1).send_keys(value)

    @allure.step("Enter address in the address box 2")
    def address_2(self):
        data = self.get_data
        value = data.get('address_2')
        self.driver.find_element(*RegisterPageLocators.ADDRESS_2).send_keys(value)

    @allure.step("Enter a city")
    def set_city(self):
        data = self.get_data
        value = data.get('set_city')
        self.driver.find_element(*RegisterPageLocators.CITY).send_keys(value)

    @allure.step("choose a state")
    def set_state(self):

        self.driver.find_element(*RegisterPageLocators.STATE).click()

        file_to_open = path_param_1() / "MyStore/state_dropdown.html"
        with open(file_to_open) as sd:

            data = self.get_data
            value = data.get('set_state')

            soup = BeautifulSoup(sd, 'html.parser')
            tags = soup.find_all("option")

            matching_tag = [tag for tag in tags if tag.string == value]

            if len(matching_tag) > 0:
                self.driver.find_element(By.XPATH, f"//option[contains(text(), '{value}')]").click()
            else:
                raise RuntimeError('There is no such state in the dropdown.')


    @allure.step("choose a country")
    def set_country(self):
        self.driver.find_element(*RegisterPageLocators.COUNTRY).click()

        file_to_open = path_param_1() / "MyStore/country_dropdown.html"
        with open(file_to_open) as sd:

            data = self.get_data
            value = data.get('set_country')

            soup = BeautifulSoup(sd, 'html.parser')
            tags = soup.find_all("option")

            matching_tag = [tag for tag in tags if tag.string == value]

            if len(matching_tag) > 0:
                self.driver.find_element(By.XPATH, f"//option[contains(text(), '{value}')]").click()
            #else:
             #   raise RuntimeError('There is no such country in the dropdown.')

    @allure.step("Enter a zip code")
    def set_zip_code(self):
        data = self.get_data
        value = data.get('set_zip')
        self.driver.find_element(*RegisterPageLocators.ZIP_CODE).send_keys(value)

    @allure.step("Enter additional information")
    def additional_info(self):
        data = self.get_data
        value = data.get('additional_info')
        self.driver.find_element(*RegisterPageLocators.ADDITIONAL_INFO).send_keys(value)

    @allure.step("Enter mobile phone number")
    def set_mobile_phone(self):
        data = self.get_data
        value = data.get('set_mobile_phone')
        self.driver.find_element(*RegisterPageLocators.MOBILE_PHONE).send_keys(value)

    @allure.step("Enter an alias")
    def set_alias(self):
        data = self.get_data
        value = data.get('set_alias')
        self.driver.find_element(*RegisterPageLocators.ADDRESS_ALIAS).send_keys(value)

    @allure.step("Click the register button")
    def click_register_button(self):
        self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    @allure.step("check if the user successfully create an account")
    def registration_success(self):
        expected_url = 'http://automationpractice.com/index.php?controller=my-account'
        assert self.driver.current_url == expected_url




