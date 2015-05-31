# coding=utf-8
from selenium.webdriver.common.by import By

__author__ = 'xubin'


class BaseLocators(object):
    TAB_HOME = (By.XPATH, '//UIATabBar[1]/UIAButton[1]')
    TAB_EXPLORE = (By.XPATH, '//UIATabBar[1]/UIAButton[2]')
    TAB_FITTINGROOM = (By.XPATH, '//UIATabBar[1]/UIAButton[3]')
    TAB_FEEDS = (By.XPATH, '//UIATabBar[1]/UIAButton[4]')
    TAB_PROFILE = (By.XPATH, '//UIATabBar[1]/UIAButton[5]')
    BTN_BACK = (By.NAME, 'Back')
    TUTORIAL1 = (By.NAME, 'Tutorial1_iP6.jpg')
    TUTORIAL2 = (By.NAME, 'Tutorial2_iP6.jpg')
    TUTORIAL3 = (By.NAME, 'Tutorial3_iP6.jpg')
    FIRST_OPEN = (By.XPATH, '//UIAScrollView[1]')


class FBLoginPageLocators(object):
    TXT_USERNAME = (By.NAME, 'email')
    TXT_PASSWORD = (By.NAME, 'pass')
    BTN_LOGIN = (By.NAME, 'login')
    BTN_CONFIRM = (By.XPATH, '//*[@value="OK"]')


class FeedsPageLocators(BaseLocators):
    BTN_FACEBOOK = (By.NAME, 'FBLoginBigIcon')
    BTN_FOLLOWING = (By.NAME, 'Following')
    BTN_YOU = (By.NAME, 'You')
    BTN_MESSAGES = (By.NAME, 'Messages')


class ProfilePageLocators(BaseLocators):
    BTN_SETTINGS = (By.NAME, 'Setting')