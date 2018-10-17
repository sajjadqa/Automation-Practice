__author__ = 'Sajjad'
import unittest
from selenium import webdriver
from BaseClasses.const import BASE_URL
from BaseClasses.dashboard_page import DashboardPage
from BaseClasses.signup_page import SignupPage


class UserBaseClass(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(BASE_URL)
        self.browser.set_page_load_timeout(30)
        self.browser.maximize_window()
        #self.browser.set_window_size(1024, 768)
        self.browser.get_screenshot_as_file("SignUp_form.png")
        self.register = SignupPage(self.browser)
        self.dashboard = DashboardPage(self.browser)

    def register_user(self, reg_fields):
        self.register.is_page_title_visible_on_page()
        self.register.fill_signup_form(reg_fields)
        self.register.submit_form_by_clicking_signup_button()

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()