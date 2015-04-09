# -*- coding:utf-8 -*-
import random
from appium.webdriver.common.touch_action import TouchAction

__author__ = 'xubin'
from selenium.webdriver.common.by import By
from CommonLib import *
from time import sleep


class DejaApp(object):
    def __init__(self, driver):
        self.wd = driver
        self.locator_first_view = '//UIAScrollView[1]'
        self.locator_home = "//UIATabBar[1]/UIAButton[1]"
        self.locator_explore = "//UIATabBar[1]/UIAButton[2]"
        self.locator_mirror = "//UIATabBar[1]/UIAButton[3]"
        self.locator_feeds = "//UIATabBar[1]/UIAButton[4]"
        self.locator_profile = "//UIATabBar[1]/UIAButton[5]"
        self.back = "Back"
        # locator from settings page
        self.locator_Settings = "Setting"
        self.locator_login_facebook = "FBLoginNormal"
        # enter main page
        try:
            self.wd.find_element_by_xpath(self.locator_first_view).click()
            sleep(0.5)
            self.wd.find_element_by_xpath(self.locator_first_view).click()
            sleep(0.5)
            self.wd.find_element_by_xpath(self.locator_first_view).click()
        except NoSuchElementException:
            raise

    def __do(self, how, locator, value=None):
        if value is None:
            self.wd.find_element(by=how, value=locator).click()
        else:
            self.wd.find_element(by=how, value=locator).send_keys(value)

    def __go_to(self, locator):
        self.__do(By.XPATH, locator)

    def go_to_home_page(self):
        self.__go_to(self.locator_home)

    def go_to_explore_page(self):
        self.__go_to(self.locator_explore)

    def go_to_mirror_page(self):
        self.__go_to(self.locator_mirror)

    def go_to_feeds_page(self):
        self.__go_to(self.locator_feeds)

    def go_to_profile_page(self):
        self.__go_to(self.locator_profile)

    def go_to_setting_page(self):
        self.go_to_profile_page()
        self.__do(By.NAME, self.locator_Settings)

    def go_to_fitting_room(self):
        self.go_to_mirror_page()
        assert self.check_element_exist_by_name("USE DEFAULT")
        self.__do(By.NAME, 'USE DEFAULT')
        if self.check_element_exist_by_name("OK"):
            self.__do(By.NAME, 'OK')
        assert self.check_element_exist_by_name("SELECT")
        self.__do(By.NAME, 'SELECT')
        self.__do(By.NAME, 'Discover Deja')


    def back_to(self):
        self.__do(By.NAME, self.back)

    def login_by_facebook(self, username, password):
        if not is_element_present(self.wd, By.NAME, 'PROFILE'):
            self.go_to_profile_page()

        self.__do(By.NAME, self.locator_login_facebook)
        sleep(4)
        self.wd.switch_to.context('WEBVIEW')
        self.__do(By.NAME, 'email', username)
        self.__do(By.NAME, 'pass', password)
        self.__do(By.NAME, 'login')
        sleep(2)
        self.__do(By.XPATH, '//*[@value="确定"]')
        sleep(2)
        self.wd.switch_to.context("NATIVE_APP")

    def check_element_exist_by_name(self, locator):
        return is_element_present(self.wd, By.NAME, locator)

    def check_element_exist_by_xpath(self, locator):
        return is_element_present(self.wd, By.NAME, locator)

    def check_element_visible_by_name(self, locator):
        return is_element_visible(self.wd, By.NAME, locator)

    def check_element_visible_by_xpath(self, locator):
        return is_element_visible(self.wd, By.XPATH, locator)

    def check_element_not_visible_by_name(self, locator):
        return is_element_not_visible(self.wd, By.NAME, locator)

    def check_element_not_visible_by_xpath(self, locator):
        return is_element_not_visible(self.wd, By.XPATH, locator)

    def do_random(self):
        window_size = self.wd.get_window_size()
        max_width = window_size["width"] - 2
        max_height = window_size["height"] - 2
        t = 0
        while 1:
            if self.check_element_visible_by_name(self.back):
                self.back_to()
            x = random.randint(1, max_width)
            y = random.randint(1, max_height)
            action = TouchAction(self.wd)
            action.tap(None, int(x), int(y)).perform()
            sleep(2)
            if t == 100:
                break
            t += 1