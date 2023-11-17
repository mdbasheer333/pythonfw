import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class AddressPage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_address(self):
        self.driver.find_element(By.LINK_TEXT, "My account").click()
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[2]/a').click()

    def add_new_address(self):
        self.driver.find_element(By.CLASS_NAME, 'add-button').click()
        self.driver.find_element(By.XPATH, '//*[@id="Address_FirstName"]').send_keys("Venkatesh")
        self.driver.find_element(By.XPATH, '//*[@id="Address_LastName"]').send_keys("Pundla")
        self.driver.find_element(By.XPATH, '//*[@id="Address_Email"]').send_keys("Venkateshbabu1106@gmail.com")
        self.driver.find_element(By.XPATH, '//*[@id="Address_Company"]').send_keys("Examity")
        c_drp = self.driver.find_element(By.XPATH, '//*[@id="Address_CountryId"]')
        country_drp = Select(c_drp)
        country_drp.select_by_visible_text("India")
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="Address_City"]').send_keys("Nellore")
        self.driver.find_element(By.XPATH, '//*[@id="Address_Address1"]').send_keys("D.NO-1645,Kapuvedi")
        self.driver.find_element(By.XPATH, '//*[@id="Address_Address2"]').send_keys("Topugunta")
        self.driver.find_element(By.XPATH, '//*[@id="Address_ZipPostalCode"]').send_keys("5243104")
        self.driver.find_element(By.XPATH, '//*[@id="Address_PhoneNumber"]').send_keys("7396601023")
        self.driver.find_element(By.XPATH, '//*[@id="Address_FaxNumber"]').send_keys("524310445")
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/form/div/div[2]/div[2]/button').click()

    def get_add_address_success_message(self):
        address_added_status = self.driver.find_element(By.XPATH, '//*[@id="bar-notification"]/div/p').text
        return address_added_status

    def close_success_popup(self):
        self.driver.find_element(By.XPATH, '//*[@id="bar-notification"]/div/span').click()
        time.sleep(2)
