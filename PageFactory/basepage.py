from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from PageFactory.pages import *

__author__ = 'xubin'


class BasePage(object):
    def __init__(self, driver):
        self.wd = driver
        self.wait = WebDriverWait(self.wd, 20)

    def back_to(self):
        try:
            self.wd.find_element(*BaseLocators.BTN_BACK).click()
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def check_exist(self, locator):
        return is_element_present(self.wd, locator)

    def check_visible(self, locator):
        return is_element_visible(self.wd, locator)

    def check_not_visible(self, locator):
        return is_element_not_visible(self.wd, locator)

