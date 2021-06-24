import time


class CustomersPage:

    def __init__(self, driver):
        self.driver = driver

    menu_option = "//ul[@class='sidebar-menu tree']"
    submenu_option = "//li[@class='treeview menu-open']/ul/li"
    btn_AddNew = "//a[@class='btn bg-blue']"
    txtbox_email = "//input[@id='Email']"
    txtbox_password = "//input[@id='Password']"
    txtbox_fname = "//input[@id='FirstName']"
    txtbox_lname = "//input[@id='LastName']"
    rdbtn_gmale = "//input[@id='Gender_Male']"
    rdbtn_gfemale = "//input[@id='Gender_Female']"
    cal_dob = "//input[@id='DateOfBirth']"
    txtbox_comp = "//input[@id='Company']"
    chkbox_tax = "//input[@id='IsTaxExempt']"
    list_newsletter = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']"
    list_custroles = "//select[@id='SelectedCustomerRoleIds']"
    txtbox_admincomment = "//textarea[@name='AdminComment']"
    btn_savecont = "//button[@name='save-continue']"
    btn_save = "//button[@name='save']"
    lnk_menuoption = "//a[@class='menu-item-link']"
    linktext = "back to customer list"
    href_customer = "//a[@href='/Admin/Customer/List']"

    txtbox_search_email = "//input[@id='SearchEmail']"
    txtbox_search_fname = "//input[@id='SearchFirstName']"
    btn_search = "//button[@id='search-customers']"

    def navigate_page(self, main_menu, sub_menu):
        menu_options = self.driver.find_elements_by_xpath("//ul[@class='sidebar-menu tree']/li[@class='treeview']/a")
        for ele in menu_options:
            print(ele.text)
            if ele.text.lower() == main_menu.lower():
                ele.click()
                time.sleep(3)
                submenu_items = self.driver.find_elements_by_xpath(self.submenu_option)
                for x in submenu_items:
                    if x.text.lower() == sub_menu.lower():
                        x.click()
                        break
                    else:
                        continue
                break
            else:
                continue

    def selectnewsletter(self, newsletter):
        self.driver.find_element_by_xpath("//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']").click()
        time.sleep(1)
        nlist = self.driver.find_elements_by_xpath("//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']")
        for ele in nlist:
            if ele.text.lower() == newsletter.lower():
                ele.click()
                break
            else:
                continue

    def select_add_new_button(self):
        self.driver.find_element_by_xpath(self.btn_AddNew).click()
        time.sleep(5)

    def add_new_customer(self, email, password, fname, lname, gendertype, dob, cname, newsletter):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.txtbox_email).send_keys(email)
        self.driver.find_element_by_xpath(self.txtbox_password).send_keys(password)
        self.driver.find_element_by_xpath(self.txtbox_fname).send_keys(fname)
        self.driver.find_element_by_xpath(self.txtbox_lname).send_keys(lname)
        if gendertype == 'male':
            self.driver.find_element_by_xpath(self.rdbtn_gmale).click()
        else:
            self.driver.find_element_by_xpath(self.rdbtn_gfemale).click()
        self.driver.find_element_by_xpath(self.cal_dob).send_keys(dob)
        self.driver.find_element_by_xpath(self.txtbox_comp).send_keys(cname)
        self.driver.find_element_by_xpath(self.chkbox_tax).click()
        # self.selectnewsletter(newsletter)
        self.driver.find_element_by_xpath(self.txtbox_admincomment).send_keys("Approve")
        self.driver.find_element_by_xpath(self.btn_savecont).click()
        time.sleep(5)

    def search_cust_byName(self, name):
        self.driver.find_element_by_xpath(self.txtbox_search_fname).send_keys(name)
        self.driver.find_element_by_xpath(self.btn_search).click()
        time.sleep(5)
        table = self.driver.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr[@role='row']")
        records = table.find_elements_by_xpath("td")
        if name.lower() in records[2].text.lower():
            assert True
            print("Customer Exists")
        else:
            assert False
            print("Customer not Exists")

    def search_cust_byEmail(self, email):
        self.driver.find_element_by_xpath(self.txtbox_search_email).send_keys(email)
        self.driver.find_element_by_xpath(self.btn_search).click()
        time.sleep(5)
        table = self.driver.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr[@role='row']")
        records = table.find_elements_by_xpath("td")
        if email.lower() in records[1].text.lower():
            assert True
            print("Customer with email Exists")
        else:
            assert False
            print("Customer not Exists")
