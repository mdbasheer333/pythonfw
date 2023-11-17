from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import allure


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def register_user(self, register_data):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.CLASS_NAME, "forcheckbox").click()
        self.driver.find_element(By.ID, "FirstName").send_keys(register_data["fname"])
        self.driver.find_element(By.ID, "LastName").send_keys(register_data["lname"])

        dob = register_data["dob"]

        drp = self.driver.find_element(By.NAME, "DateOfBirthDay")
        day_drp = Select(drp)
        day_drp.select_by_index(int(dob.split("-")[0]))

        drp1 = self.driver.find_element(By.NAME, "DateOfBirthMonth")
        month_drp = Select(drp1)
        month_drp.select_by_visible_text(dob.split("-")[1])

        drp2 = self.driver.find_element(By.NAME, "DateOfBirthYear")
        year_drp = Select(drp2)
        year_drp.select_by_value(dob.split("-")[2])

        self.driver.find_element(By.NAME, "Email").send_keys(register_data["email"])

        self.driver.find_element(By.NAME, "Company").send_keys(register_data["company"])
        self.driver.find_element(By.NAME, "Password").send_keys(register_data["password"])
        self.driver.find_element(By.NAME, "ConfirmPassword").send_keys(register_data["password"])
        self.driver.find_element(By.ID, "register-button").click()
