from CommonLib import *
from ObjectRepository.locators import *
from PageFactory.basepage import BasePage

__author__ = 'xubin'


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

