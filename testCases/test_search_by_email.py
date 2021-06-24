import pytest

from pageObjects.CustomersPage import CustomersPage
from pageObjects.LoginPage import LoginPage


class test_search_by_email:
    @pytest.mark.regression
    def test_005_Search(self, setup):
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

        self.cp.search_cust_byEmail("adads")

        self.driver.close()
        self.logger.info("--------------Test003-End-------------------")