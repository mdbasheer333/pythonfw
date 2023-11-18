from selenium.webdriver.common.by import By
from ui.locators.locators import Locator

lnkReg = Locator(By.LINK_TEXT, "Register", "lnkReg")
forChk = Locator(By.CLASS_NAME, "forcheckbox", "forChk")
fname = Locator(By.ID, "FirstName", "fname")
lname = Locator(By.ID, "LastName", "lname")
drp = Locator(By.NAME, "DateOfBirthDay", "drp")
drp1 = Locator(By.NAME, "DateOfBirthMonth", "drp1")
drp2 = Locator(By.NAME, "DateOfBirthYear", "drp2")
mail = Locator(By.NAME, "Email", "mail")
cmpny = Locator(By.NAME, "Company", "cmpny")
pwd = Locator(By.NAME, "Password", "pwd")
cpwd = Locator(By.NAME, "ConfirmPassword", "cpwd")
rgbtn = Locator(By.ID, "register-button", "rgbtn")
