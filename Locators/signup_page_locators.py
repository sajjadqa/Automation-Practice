__author__ = 'Sajjad'
from selenium.webdriver.common.by import By

class SignupPageLocators(object):
    PAGE_TITLE = (By.CSS_SELECTOR, "div[class='col-md-8 col-md-offset-2'] h1")
    COMPANY_NAME = (By.CSS_SELECTOR, '[name="broker_name"]')
    COUNTRY = (By.CSS_SELECTOR, 'select[name="broker_address_country"]')
    YOUR_INSLY_ADDRESS = (By.CSS_SELECTOR, 'input[name="broker_tag"]')
    COMPANY_PROFILE = (By.CSS_SELECTOR, 'select[name="prop_company_profile"]')
    NUMBER_OF_EMPLOYEES = (By.CSS_SELECTOR, 'select[name="prop_company_no_employees"]')
    HOW_WOULD_YOU_DESCRIBE_YOURSELF = (By.CSS_SELECTOR, 'select[name="prop_company_person_description"]')
    WORK_EMAIL = (By.CSS_SELECTOR, 'input[name="broker_admin_email"]')
    ACCOUNT_MANAGER_NAME = (By.CSS_SELECTOR, 'input[name="broker_admin_name"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="broker_person_password"]')
    PASSWORD_REPEAT = (By.CSS_SELECTOR, 'input[id="broker_person_password_repeat"]')
    SUGGEST_A_SECURE_PASSWORD = (By.CSS_SELECTOR, '#broker_person_password +a')
    REMEMBER_PASSWORD = (By.CSS_SELECTOR, '#insly_alert b')
    OK_BUTTON_ON_PASSWORD_DIALOGUE = (By.CSS_SELECTOR, '.ui-dialog-buttonset button')
    PHONE = (By.CSS_SELECTOR, '[id="broker_admin_phone"]')
    TERMS_AND_CONDITIONS_CHECKBOX = (By.CSS_SELECTOR, '[id="agree_termsandconditions"] +span')
    TERMS_AND_CONDITIONS_LINK=(By.CSS_SELECTOR,'[id="agree_termsandconditions"]  +span+a')
    TERMS_AND_CONDITIONS_I_AGREE_BUTTON = (By.CSS_SELECTOR, '.ui-dialog-buttonset button[class="primary"]')
    TERMS_AND_CONDITIONS_CLOSE_BUTTON = (By.CSS_SELECTOR, '[class="ui-dialog-buttonset"] button:nth-of-type(2)')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '[id="agree_privacypolicy"]  +span')
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, '[id="agree_privacypolicy"]  +span+a')
    PRIVACY_DIALOGUE_CLOSED = (By.CSS_SELECTOR, 'body>div:nth-of-type(2) a span')
    AGREE_DATA_PROCESSING = (By.CSS_SELECTOR, '[id="agree_data_processing"] +span')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, '.primary.signup-btn')
    ERROR_DIALOG = (By.CSS_SELECTOR, '.ui-dialog[role="dialog"]')
    ERROR_MESSAGES = (By.CSS_SELECTOR, '#insly-alert-errors')
    PHONE_ERROR_MESSAGE = (By.CSS_SELECTOR, '#insly-alert-errors>b:nth-of-type(8)')