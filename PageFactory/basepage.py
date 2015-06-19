from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from PageFactory.pages import *

__author__ = 'xubin'


class BasePage(object):
    def __init__(self, driver):
        self.wd = driver
        self.wait = WebDriverWait(self.wd, 20)

    def check_exist(self, locator):
        return is_element_present(self.wd, locator)

    def check_visible(self, locator):
        return is_element_visible(self.wd, locator)

    def check_not_visible(self, locator):
        return is_element_not_visible(self.wd, locator)

    def check_exist_by_text(self, text):
        return is_element_present(self.wd, (By.NAME, text))
