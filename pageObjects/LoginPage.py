from selenium import webdriver

class LoginPage:
    txtbox_email = "//input[@type = 'email']"
    txtbox_password = "//input[@type = 'password']"
    chkbox_remember = "//input[@id = 'RememberMe']"
    btn_Login = "//input[@value = 'Log in']"
    lnktxt_Logout = "Logout"

    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element_by_xpath(self.txtbox_email).clear()
        self.driver.find_element_by_xpath(self.txtbox_email).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtbox_password).clear()
        self.driver.find_element_by_xpath(self.txtbox_password).send_keys(password)

    def login_to_home(self):
        self.driver.find_element_by_xpath(self.btn_Login).click()
