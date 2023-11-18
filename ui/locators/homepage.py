from selenium.webdriver.common.by import By
from ui.locators.locators import Locator

txt_search = Locator(By.ID, "small-searchterms", "txt_search")
btn_search = Locator(By.XPATH, "//button[text()='Search']", "btn_search")
chkBox_adv_search = Locator(By.NAME, 'advs', "chkBox_adv_search")
