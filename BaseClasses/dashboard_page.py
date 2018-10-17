__author__ = 'Sajjad'
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.dashboard_page_locators import DashboardPageLocators
from BaseClasses.const import BASE_URL, TARGET_URL
from BaseClasses.insly_base_page import BasePage


class DashboardPage(BasePage):

    url = os.path.join(BASE_URL, "dashboard")

    def is_browser_on_page(self):
        WebDriverWait(self.browser, 120).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user-info')))
        return self.browser.find_element(*DashboardPageLocators.USER_INFO).is_displayed()

    def get_current_url(self):
        WebDriverWait(self.browser, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user-info')))
        #assert get_registration_fields().get("insly_address") in self.browser.current_url
        return self.browser.current_url

    def compare_url(self, reg_fields):
        url = "https://{}.{}/dashboard".format(reg_fields.get('insly_address'), TARGET_URL)
        return url