from selenium import webdriver
import pytest
from ui.pageobjects.AddressPage import AddressPage
from ui.pageobjects.LoginPage import LoginPage
import os

class TestLogin:

    @pytest.mark.regression
    def test_login(self, ui_browser):
        url = os.getenv("env_web")
        ui_browser.get(url)
        login_page = LoginPage(ui_browser)
        login_page.login_to_app("dummy@gmail.com", "bash#1234")
        login_page.logout()
        assert 1==2, "1 is 2 now a days"
