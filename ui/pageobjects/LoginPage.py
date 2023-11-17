from selenium.webdriver.common.by import By
import time
import allure

from ui.pageobjects.BasePage import BasePage


class LoginPage(BasePage):
    __link_login = (By.LINK_TEXT, "Log in")
    __txt_username = (By.ID, "Email")
    __txt_password = (By.XPATH, '//*[@id="Password"]')
    __btn_login = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button')
    __link_logout = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        # self.driver = driver

    def login_to_app(self, user_name, password):
        # self.driver.find_element(*self.__link_login).click()
        # self.wait_for_element(self.__link_login)
        self.click(self.__link_login)
        # self.driver.find_element(*self.__txt_username).send_keys(user_name)
        self.enter(self.__txt_username, user_name)
        self.enter(self.__txt_password, password)
        # self.driver.find_element(*self.__txt_password).send_keys(password)
        # self.driver.find_element(*self.__btn_login).click()
        self.click(self.__btn_login)

    def logout(self):
        # self.wait_for_element(self.__link_logout)
        # self.driver.find_element(*self.__link_logout).click()
        self.wait_click(self.__link_logout)
