import allure

from ui.pageobjects.BasePage import BasePage
from ui.locators.loginpage import *


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    @allure.step
    def login_to_app(self, user_name, password):
        self.click(link_login)
        self.enter(txt_username, user_name)
        self.enter(txt_password, password)
        self.click(btn_login)

    def logout(self):
        self.wait_click(link_logout)
