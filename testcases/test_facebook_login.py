from appium import SauceTestCase, on_platforms
from CommonLib.NormalAction import DejaApp
from Environment import platforms

__author__ = 'xubin'


# def test_random(self):
# deja = DejaApp(self.driver)
#     deja.do_random()
@on_platforms(platforms)
class SmokeTestingOnSauceTests(SauceTestCase):
    def test_user_can_login_facebook(self):
        deja = DejaApp(self.driver)
        deja.go_to_home_page()
        deja.go_to_setting_page()
        assert not deja.check_element_exist_by_name("Sign Out")
        deja.back_to()
        deja.login_by_facebook("dejafashion88@gmail.com", "mozatm2u")
        assert deja.check_element_exist_by_name("PROFILE")
        deja.go_to_setting_page()
        assert deja.check_element_exist_by_name("Sign Out")
