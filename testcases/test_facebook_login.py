from appium import SauceTestCase, on_platforms
from Environment import platforms
from PageFactory.pages import *

__author__ = 'xubin'


# def test_random(self):
# deja = DejaApp(self.driver)
# deja.do_random()
@on_platforms(platforms)
class SmokeTestingOnSauceTests(SauceTestCase):
    def test_user_can_login_facebook(self):
        sp = StartPage(self.driver)
        explore_page = sp.finish_tutorial()
        feeds_page = CommonPage(self.driver).go_to_feeds_page()
        feeds_page = feeds_page.login_by_facebook(
            'mozatqa90@gmail.com', 'mozatm2u')