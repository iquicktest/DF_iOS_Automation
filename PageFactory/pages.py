from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CommonLib import *
from ObjectRepository.locators import *
from time import sleep

__author__ = 'xubin'


class BasePage(object):
    def __init__(self, driver):
        self.wd = driver
        self.wait = WebDriverWait(self.wd, 20)

    def go_to_home_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_HOME).click()
            return HomePage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_explore_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_EXPLORE).click()
            return ExplorePage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_fitting_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_FITTINGROOM).click()
            return FittingRoomPage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_feeds_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_FEEDS).click()
            return FeedsPage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_profile_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_PROFILE).click()
            return ProfilePage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_setting_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_PROFILE).click()
            self.wd.find_element(*ProfilePageLocators.BTN_SETTINGS).click()
            return SettingPage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

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

    def login_by_facebook(self, username, password):
        """

        :rtype : FeedsPage
        """
        self.go_to_feeds_page()
        self.wd.find_element(*FeedsPageLocators.BTN_FACEBOOK).click()
        sleep(4)
        self.wd.switch_to.context('WEBVIEW')
        try:
            self.wd.find_element(*FBLoginPageLocators.TXT_USERNAME).send_keys(username)
            self.wd.find_element(*FBLoginPageLocators.TXT_PASSWORD).send_keys(password)
            self.wd.find_element(*FBLoginPageLocators.BTN_LOGIN).click()
            sleep(2)
            self.wd.find_element(*FBLoginPageLocators.BTN_CONFIRM).click()
            sleep(2)
            self.wd.switch_to.context("NATIVE_APP")
            return FeedsPage(self.wd)
        except NoSuchElementException:
            return None


class HomePage(BasePage):
    pass


class FeedsPage(BasePage):
    pass


class FittingRoomPage(BasePage):
    pass


class ExplorePage(BasePage):
    pass


class ProfilePage(BasePage):
    pass


class SettingPage(BasePage):
    pass


class StartPage(BasePage):
    def finish_tutorial(self):
        try:
            self.wd.find_element(*BaseLocators.TUTORIAL1).click()
            self.wd.find_element(*BaseLocators.TUTORIAL2).click()
            self.wd.find_element(*BaseLocators.TUTORIAL3).click()
        except NoSuchElementException:
            raise
        return ExplorePage(self.wd)

