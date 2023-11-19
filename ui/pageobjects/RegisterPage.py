import allure
from selenium.webdriver.support.select import Select

from ui.locators.registerpage import *
from ui.pageobjects.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def register_user(self, register_data):
        self.click(lnkReg)
        self.click(forChk)
        self.enter(fname, "bash")
        self.enter(lname, "mohammad")
        dob = register_data["dob"]
        day_drp = Select(drp.get_web_element(self.driver))
        day_drp.select_by_index(int(dob.split("-")[0]))
        month_drp = Select(drp1.get_web_element(self.driver))
        month_drp.select_by_visible_text(dob.split("-")[1])
        year_drp = Select(drp2.get_web_element(self.driver))
        year_drp.select_by_value(dob.split("-")[2])
        self.enter(mail, "dummy1234@gmail.com")
        self.enter(cmpny, "orc")
        self.enter(pwd, "bash1234")
        self.enter(cpwd, "bash1234")
        self.click(rgbtn)
