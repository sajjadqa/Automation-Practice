__author__ = 'Sajjad'
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseClasses.const import BASE_URL
from BaseClasses.insly_base_page import BasePage
from Locators.signup_page_locators import SignupPageLocators
from BaseClasses.helpers import select_val_from_drop_down, open_link


class SignupPage(BasePage):

    url = os.path.join(BASE_URL, "signup")
    scroll_down = '$(".privacy-policy-dialog > div").animate({ scrollTop: $("#document-content").height()}, 1000);'

    def is_page_title_visible_on_page(self):
        assert "Sign up and start using" in self.browser.find_element(*SignupPageLocators.PAGE_TITLE).text

    def fill_signup_form(self, reg_fields):
        if "company_name" in reg_fields:
            self.browser.find_element(*SignupPageLocators.COMPANY_NAME).send_keys(reg_fields["company_name"])
        if "country" in reg_fields:
            select_val_from_drop_down(self, "#broker_address_country", reg_fields["country"], use_jquery=True)
        if "insly_address" in reg_fields:
            self.browser.find_element(*SignupPageLocators.YOUR_INSLY_ADDRESS).send_keys(reg_fields["insly_address"])
        if "company_profile" in reg_fields:
            select_val_from_drop_down(self, "#prop_company_profile", reg_fields["company_profile"], use_jquery=True)
        if "number_of_employees" in reg_fields:
            select_val_from_drop_down(self, "#prop_company_no_employees", reg_fields["number_of_employees"], use_jquery=True)
        if "describe_yourself" in reg_fields:
            select_val_from_drop_down(self, "#prop_company_person_description", reg_fields["describe_yourself"], use_jquery=True)
        if "work_email" in reg_fields:
            self.browser.find_element(*SignupPageLocators.WORK_EMAIL).send_keys(reg_fields["work_email"])
        if "account_manager_name" in reg_fields:
            self.browser.find_element(*SignupPageLocators.ACCOUNT_MANAGER_NAME).send_keys(reg_fields["account_manager_name"])
        if "password" in reg_fields:
            self.browser.find_element(*SignupPageLocators.SUGGEST_A_SECURE_PASSWORD).click()
            open_link(self, '#broker_person_password +a', reg_fields["suggest_secure_password"])
            password = self.browser.find_element(*SignupPageLocators.REMEMBER_PASSWORD).text
            print("Password for this fake user:", password)
            self.browser.find_element(*SignupPageLocators.OK_BUTTON_ON_PASSWORD_DIALOGUE).click()
            #self.browser.find_element(*SignupPageLocators.PASSWORD).clear()
        if "repeat_password" in reg_fields:
            #self.browser.find_element(*SignupPageLocators.PASSWORD_REPEAT).clear()
            self.browser.find_element(*SignupPageLocators.PASSWORD_REPEAT).send_keys(reg_fields["repeat_password"])
        if "phone" in reg_fields:
            self.browser.find_element(*SignupPageLocators.PHONE).send_keys(reg_fields["phone"])
        if "terms_and_condition" in reg_fields:
            self.browser.find_element(*SignupPageLocators.TERMS_AND_CONDITIONS_CHECKBOX).click()
            open_link(self, '#agree_termsandconditions +span+a', reg_fields["terms_condition_link"])
            WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#document-content')))
            self.browser.execute_script(self.scroll_down)
            self.browser.find_element(*SignupPageLocators.TERMS_AND_CONDITIONS_I_AGREE_BUTTON).click()
        if "privacy_policy" in reg_fields:
            self.browser.find_element(*SignupPageLocators.PRIVACY_POLICY).click()
            open_link(self, '#agree_privacypolicy +span+a', reg_fields["privacy_policy_link"])
            WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#document-content')))
            self.browser.execute_script(self.scroll_down)
            time.sleep(3)
            WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#document-content')))
            self.browser.find_element(*SignupPageLocators.PRIVACY_DIALOGUE_CLOSED).click()
        if "agree_data_processing" in reg_fields:
            self.browser.find_element(*SignupPageLocators.AGREE_DATA_PROCESSING).click()
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.primary.signup-btn')))

    def submit_form_by_clicking_signup_button(self):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.primary.signup-btn')))
        self.browser.find_element(*SignupPageLocators.SIGNUP_BUTTON).click()

    def error_messages(self):
        WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#insly-alert-errors')))
        errors = self.browser.find_elements(*SignupPageLocators.ERROR_MESSAGES)
        error_list = []
        for error_text in errors:
            error_list.append(error_text.text)
        return str(error_list)