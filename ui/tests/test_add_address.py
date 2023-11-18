import os

import pytest

from ui.pageobjects.AddressPage import AddressPage
from ui.pageobjects.LoginPage import LoginPage
from ui.utils.ExcelUtil import read_excel_data
import logging


class TestAddAddress:

    @pytest.mark.sanity
    def test_edit_address(self, browser, config):
        url = config["env_web"]
        browser.get(url)

    @pytest.mark.sanity
    @pytest.mark.parametrize('test_data',
                             read_excel_data('registerUser'))
    def test_add_address(self, browser, test_data, config):
        url = config["env_web"]
        browser.get(url)
        logging.getLogger().info(f"data is {test_data}")
        login_page = LoginPage(browser)
        login_page.login_to_app(os.getenv("app_user_id"), os.getenv("app_password"))

        address_page = AddressPage(browser)
        address_page.navigate_to_address()

        address_data = {
        }

        address_page.add_new_address()

        ex_address_status = 'The new address has been added successfully.'
        act_address_status = address_page.get_add_address_success_message()
        assert ex_address_status == act_address_status, 'mis matched address'

        address_page.close_success_popup()

        login_page.logout()
