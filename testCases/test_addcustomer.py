import pytest

from pageObjects.CustomersPage import CustomersPage
from pageObjects.LoginPage import LoginPage
from utilities.customlogger import LogGen
from utilities.readproperty import ReadConfig


class Test_AddCustomer:

    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_003_AddCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("--------------Test003-Navigation-started-------------------")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login_to_home()
        self.cp = CustomersPage(self.driver)
        self.cp.navigate_page('Customers', 'Customers')
        homepage_title = self.driver.title
        if "nopCommerce administration" in homepage_title:
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False
        self.cp.select_add_new_button()
        self.cp.add_new_customer("adads@gmail.com", "testing", "Mark", "L", "male", "2/4/2021", "newsoft",
                                 "Test store 2")
        self.driver.close()
        self.logger.info("--------------Test003-End-------------------")