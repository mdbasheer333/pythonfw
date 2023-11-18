import json
import os

import pytest

from ui.pageobjects.RegisterPage import RegisterPage


class TestRegisterUser:

    @pytest.mark.smoke
    def test_register_user(self, config, browser):
        url = config["env_web"]
        browser.get(url)

        register_page_obj = RegisterPage(browser)

        with open("sample.json", 'r') as json_file:
            register_data = json.load(json_file)
        register_data = register_data

        register_page_obj.register_user(register_data)
        # time.sleep(30)
        # exp_result = "Your registration completed"
        # act_result = driver.find_element_by_class_name("result").text
        # assert exp_result == act_result, "reg not success"
