from selenium.webdriver.common.by import By



class RegisterPageLocators:

    CREATE_ACC_EMAIL = By.ID, 'email_create'
    CREATE_ACC_BUTTON = By.ID, 'SubmitCreate'
    RADIO_MR = By.XPATH, '//label[@for="id_gender1"]'
    RADIO_MRS = By.XPATH, '//label[@for="id_gender2"]'
    SET_FIRST_NAME = By.NAME, 'customer_firstname'
    SET_LAST_NAME = By.NAME, 'customer_lastname'
    SET_EMAIL = By.ID, 'email'
    SET_PASSWORD = By.ID, 'passwd'
    DAY_OF_BIRTH = By.ID, 'days'
    MONTH_OF_BIRTH = By.ID, 'months'
    YEAR_OF_BIRTH = By.ID, 'years'
    NEWSLETTER_CB = By.ID, 'uniform-newsletter'
    OFFER_CB = By.ID, 'uniform-optin'
    FIRST_NAME_ADS = By.ID, 'firstname'
    LAST_NAME_ADS = By.ID, 'lastname'
    COMPANY = By.ID, 'company'
    ADDRESS_1 = By.ID, 'address1'
    ADDRESS_2 = By.ID, 'address2'
    CITY = By.ID, 'city'
    STATE = By.ID, 'uniform-id_state'
    ZIP_CODE = By.ID, 'postcode'
    COUNTRY = By.ID, 'id_country'
    ADDITIONAL_INFO = By.ID, 'other'
    HOME_PHONE = By.ID, 'phone'
    MOBILE_PHONE = By.ID, 'phone_mobile'
    ADDRESS_ALIAS = By.ID, 'alias'
    REGISTER_BUTTON = By.ID, 'submitAccount'


class LogInLocators:
    LOGIN_EMAIL = By.ID, 'email'
    LOGIN_PW = By.ID, 'passwd'
    LOGIN_BUTTON = By.ID, 'SubmitLogin'


class PersonalInfoLocators:

    STATE_OPTIONS = By.CLASS_NAME, 'selector focus hover'
    PERSONAL_INFO_BUTTON = By.XPATH, '//a[@title="Information"]'
    RADIO_MR_PI = By.XPATH, '//input[@id="id_gender1" and @checked="checked"]'
    RADIO_MRS_PI = By.XPATH, '//input[@id="id_gender2" and @checked="checked"]'

























