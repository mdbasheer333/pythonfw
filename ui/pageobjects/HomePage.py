from selenium.webdriver.common.by import By
import time
import allure

from ui.pageobjects.BasePage import BasePage
from ui.locators.homepagelocator import *


class HomePage(BasePage):
    __txt_search = (By.ID, "small-searchterms")
    __btn_search = (By.XPATH, "//button[text()='Search']")
    __chkBox_adv_search = (By.NAME, 'advs')

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def search_a_phone_product(self):
        self.enter(txt_user_name, "phone")
        self.click(self.__btn_search)
        self.click(self.__chkBox_adv_search)
