from selenium.webdriver.common.by import By
from ui.locators.locators import Locator

txt_user_name = Locator(By.ID, "txtUsername", "user name field")
txt_password = Locator(By.ID, "txtPassword", "password field")
btn_Login = Locator(By.NAME, "Submit", "Login button")

lnk_welcome = Locator(By.PARTIAL_LINK_TEXT, "Welcome", "Welcome link")
lnk_logout = Locator(By.LINK_TEXT, "Logout", "Logout link")

lnk_my_info = Locator(By.LINK_TEXT, "My Info", "My Info link")
lnk_emergency_contact = Locator(By.LINK_TEXT, "Emergency Contacts", "Emergency Contacts link")
btn_add_emergency_contact = Locator(By.ID, "btnAddContact", "Add Emergency Contacts button")
txt_name = Locator(By.ID, "emgcontacts_name", "emgcontacts_name filed")
txt_rel_type = Locator(By.ID, "emgcontacts_relationship", "emgcontacts_relationship field")
txt_home_phone = Locator(By.ID, "emgcontacts_homePhone", "emgcontacts_homePhone field")
txt_mob_phone = Locator(By.ID, "emgcontacts_mobilePhone", "emgcontacts_mobilePhone field")
txt_wrk_phone = Locator(By.ID, "emgcontacts_workPhone", "emgcontacts_workPhone field")
btn_save_my_info = Locator(By.ID, "btnSaveEContact", "Emergency Contacts save button")

lnk_leave = Locator(By.LINK_TEXT, "Leave", "Leave link")
lnk_Apply = Locator(By.LINK_TEXT, "Apply", "Apply link")
drpdown_leaveType = Locator(By.ID, "applyleave_txtLeaveType", "drpdown_leaveType")

lnk_dashboard = Locator(By.LINK_TEXT, "Dashboard", "Dashboard board link")
lnk_applyleave = Locator(By.XPATH, "//span[text()='Apply Leave']/..", "apply leave link in dashboard")
