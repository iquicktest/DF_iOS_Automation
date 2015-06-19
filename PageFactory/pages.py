from time import sleep
from selenium.webdriver.common.by import By
from CommonLib import *
from PageFactory.basepage import BasePage

__author__ = 'xubin'


class HomePage(BasePage):
    pass


class SettingPage(BasePage):
    SWH_SAVE_ORIGIN_STYLE_IMAGES = (By.NAME, 'Save Original Style Images')
    LBE_CLEAR_CACHE = (By.NAME, 'Clear Image Cache')
    LBE_PUSH_NOTIFICATION = (By.NAME, 'Push Notifications')
    LBE_SING_OUT = (By.NAME, 'Sign Out')

    def check_is_login(self):
        return self.check_exist(self.LBE_SING_OUT)


class FeedsPage(BasePage):
    BTN_FACEBOOK = (By.NAME, 'FBLoginBigIcon')
    BTN_FOLLOWING = (By.NAME, 'Following')
    BTN_YOU = (By.NAME, 'You')
    BTN_MESSAGES = (By.NAME, 'Messages')
    TXT_USERNAME = (By.NAME, 'email')
    TXT_PASSWORD = (By.NAME, 'pass')
    BTN_LOGIN = (By.NAME, 'login')
    BTN_CONFIRM = (By.XPATH, '//*[@value="OK"]')

    def login_by_facebook(self, username, password):
        """

        :rtype : FeedsPage
        """
        self.wd.find_element(*self.BTN_FACEBOOK).click()
        sleep(4)
        self.wd.switch_to.context('WEBVIEW')
        try:
            self.wd.find_element(*self.TXT_USERNAME).send_keys(username)
            self.wd.find_element(*self.TXT_PASSWORD).send_keys(password)
            self.wd.find_element(*self.BTN_LOGIN).click()
            sleep(2)
            self.wd.find_element(*self.BTN_CONFIRM).click()
            sleep(2)
            self.wd.switch_to.context("NATIVE_APP")
            return self
        except NoSuchElementException:
            return None


class FittingRoomPage(BasePage):
    pass


class ExplorePage(BasePage):
    pass


class ProfilePage(BasePage):
    BTN_SETTINGS = (By.NAME, 'Setting')

    def go_to_setting_page(self):
        try:
            self.wd.find_element(*self.BTN_SETTINGS).click()
            return SettingPage(self.wd)
        except NoSuchElementException:
            print '[Element Not Exist]: No Such Element ' + self.BTN_SETTINGS
            return None


class StartPage(BasePage):
    TUTORIAL1 = (By.NAME, 'Tutorial1_iP6.jpg')
    TUTORIAL2 = (By.NAME, 'Tutorial2_iP6.jpg')
    TUTORIAL3 = (By.NAME, 'Tutorial3_iP6.jpg')
    FIRST_OPEN = (By.XPATH, '//UIAScrollView[1]')

    def finish_tutorial(self):
        try:
            self.wd.find_element(*self.TUTORIAL1).click()
            self.wd.find_element(*self.TUTORIAL2).click()
            self.wd.find_element(*self.TUTORIAL3).click()
            return ExplorePage(self.wd)
        except NoSuchElementException:
            print 'No Such Element'
            return None


class CommonPage(BasePage):
    TAB_HOME = (By.XPATH, '//UIATabBar[1]/UIAButton[1]')
    TAB_EXPLORE = (By.XPATH, '//UIATabBar[1]/UIAButton[2]')
    TAB_FITTINGROOM = (By.XPATH, '//UIATabBar[1]/UIAButton[3]')
    TAB_FEEDS = (By.XPATH, '//UIATabBar[1]/UIAButton[4]')
    TAB_PROFILE = (By.XPATH, '//UIATabBar[1]/UIAButton[5]')
    BTN_BACK = (By.NAME, 'Back')

    def back_to(self):
        try:
            self.wd.find_element(*self.BTN_BACK).click()
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_home_page(self):
        try:
            self.wd.find_element(*self.TAB_HOME).click()
            return HomePage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_explore_page(self):
        try:
            self.wd.find_element(*self.TAB_EXPLORE).click()
            return ExplorePage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_fitting_page(self):
        try:
            self.wd.find_element(*self.TAB_FITTINGROOM).click()
            return FittingRoomPage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_feeds_page(self):
        try:
            self.wd.find_element(*self.TAB_FEEDS).click()
            return FeedsPage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None

    def go_to_profile_page(self):
        try:
            self.wd.find_element(*self.TAB_PROFILE).click()
            return ProfilePage(self.wd)
        except NoSuchElementException:
            print 'NoSuchElementException'
            return None