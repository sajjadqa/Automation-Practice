__author__ = 'Sajjad'

import requests
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.browser = driver
        self.wait = WebDriverWait(driver, 30)

    def is_page_fully_loaded(self):
        current_url = self.browser.current_url
        resp = requests.get(current_url)

