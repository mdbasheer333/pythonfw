from ui.locators.homepage import *
from ui.pageobjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def search_a_phone_product(self):
        self.enter(txt_search, "phone")
        self.click(btn_search)
        self.click(chkBox_adv_search)
