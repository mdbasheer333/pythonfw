from selenium.webdriver.common.by import By
from ui.locators.locators import Locator

link_login = Locator(By.LINK_TEXT, "Log in", "__link_login")
txt_username = Locator(By.ID, "Email", "__txt_username")
txt_password = Locator(By.XPATH, '//*[@id="Password"]', "__txt_password")
btn_login = Locator(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button',
                    "__btn_login")
link_logout = Locator(By.LINK_TEXT, "Log out", "__link_logout")
