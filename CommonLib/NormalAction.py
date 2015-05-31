# -*- coding:utf-8 -*-
import random
from appium.webdriver.common.touch_action import TouchAction
from ObjectRepository.locators import BaseLocators, ProfilePageLocators, FeedsPageLocators, FBLoginPageLocators

__author__ = 'xubin'
from selenium.webdriver.common.by import By
from CommonLib import *
from time import sleep


class DejaApp(object):
    def __init__(self, driver):
        self.wd = driver
        # enter main page
        try:
            self.wd.find_element(*BaseLocators.FIRST_OPEN)
            sleep(0.5)
            self.wd.find_element(*BaseLocators.FIRST_OPEN)
            sleep(0.5)
            self.wd.find_element(*BaseLocators.FIRST_OPEN)
        except NoSuchElementException:
            raise

    def go_to_home_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_HOME)
        except NoSuchElementException:
            raise

    def go_to_explore_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_EXPLORE)
        except NoSuchElementException:
            raise

    def go_to_fitting_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_FITTINGROOM)
        except NoSuchElementException:
            raise

    def go_to_feeds_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_FEEDS)
        except NoSuchElementException:
            raise

    def go_to_profile_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_PROFILE)
        except NoSuchElementException:
            raise

    def go_to_setting_page(self):
        try:
            self.wd.find_element(*BaseLocators.TAB_PROFILE)
            self.wd.find_element(*ProfilePageLocators.BTN_SETTINGS)
        except NoSuchElementException:
            raise


    def back_to(self):
        try:
            self.wd.find_element(*BaseLocators.BTN_BACK)
        except NoSuchElementException:
            raise

    def login_by_facebook(self, username, password):
        self.go_to_feeds_page()
        self.wd.find_element(*FeedsPageLocators.BTN_FACEBOOK)
        sleep(4)
        self.wd.switch_to.context('WEBVIEW')
        self.wd.find_element(*FBLoginPageLocators.TXT_USERNAME).send_keys(username)
        self.wd.find_element(*FBLoginPageLocators.TXT_PASSWORD).send_keys(password)
        self.wd.find_element(*FBLoginPageLocators.BTN_LOGIN)
        sleep(2)
        self.wd.find_element(*FBLoginPageLocators.BTN_CONFIRM)
        sleep(2)
        self.wd.switch_to.context("NATIVE_APP")

    def check_element_exist_by_locator(self, locator):
        return is_element_present(self.wd, locator)

    def check_element_visible_by_locator(self, locator):
        return is_element_visible(self.wd, locator)

    def check_element_not_visible_by_locator(self, locator):
        return is_element_not_visible(self.wd, locator)

    def do_random(self):
        window_size = self.wd.get_window_size()
        max_width = window_size["width"] - 2
        max_height = window_size["height"] - 2
        t = 0
        while 1:
            if self.check_element_visible_by_locator(*BaseLocators.BTN_BACK):
                self.back_to()
            x = random.randint(1, max_width)
            y = random.randint(1, max_height)
            action = TouchAction(self.wd)
            action.tap(None, int(x), int(y)).perform()
            sleep(2)
            if t == 100:
                break
            t += 1