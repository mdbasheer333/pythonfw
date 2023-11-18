import time

from selenium.webdriver.support.select import Select

from ui.locators.addresspage import *
from ui.pageobjects.BasePage import BasePage


class AddressPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_address(self):
        self.click(my_act)
        self.click(link)

    def add_new_address(self):
        self.click(addBtn)
        self.enter(fname, "basheer")
        self.enter(lname, "mohammad")
        self.enter(mail, "dummy1234@gmail.com")
        self.enter(adrCmpy, "bash")
        country_drp = Select(c_drp.get_web_element(self.driver))
        country_drp.select_by_visible_text("India")
        time.sleep(2)
        self.enter(adrCity, "hyd")
        self.enter(adr1, "borabanda")
        self.enter(adr2, "haji mastan")
        self.enter(zip, "123456")
        self.enter(phone_num, "13245648")
        self.enter(fax, "78798798")
        self.click(rgBtn);

    def get_add_address_success_message(self):
        return address_added_status.get_web_element(self.driver).text

    def close_success_popup(self):
        self.click(notification)
        time.sleep(2)
