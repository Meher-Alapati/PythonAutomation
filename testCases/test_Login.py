import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen


class Test_LoginTests:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_001_login_verify_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("--------------Test001-homepage-title-------------------")
        app_title = self.driver.title
        if app_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            assert False

        self.logger.info("--------------Test001-homepage-title-------------------")

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_002_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("--------------Test002-Login-started-------------------")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login_to_home()
        homepage_title = self.driver.title
        if "nopCommerce administration" in homepage_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False

        self.logger.info("--------------Test002-Login-End-------------------")
