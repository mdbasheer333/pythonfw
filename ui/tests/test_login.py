import os

import pytest

from ui.pageobjects.LoginPage import LoginPage


@pytest.mark.regression
def test_login(config, browser):
    url = config["env_web"]
    browser.get(url)
    login_page = LoginPage(browser)
    login_page.login_to_app("dummy@gmail.com", "bash#1234")
    login_page.logout()
    assert 1 == 2, "1 is 2 now a days"
