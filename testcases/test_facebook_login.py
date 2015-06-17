from appium import SauceTestCase, on_platforms
from Environment import platforms
from PageFactory.pages import *

__author__ = 'xubin'


@on_platforms(platforms)
class SmokeTestingOnSauceTests(SauceTestCase):
    def test_user_can_login_facebook(self):
        sp = StartPage(self.driver)
        sp.finish_tutorial()
        common_page = CommonPage(self.driver)
        feeds_page = common_page.go_to_feeds_page()
        feeds_page = feeds_page.login_by_facebook(
            'mozatqa90@gmail.com', 'mozatm2u')
        common_page.go_to_profile_page()
