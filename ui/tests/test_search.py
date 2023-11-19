import os

import pytest

from ui.pageobjects.HomePage import HomePage
from ui.utils.CustomAssert import CustomAssert


@pytest.mark.smoke
def test_search(config, browser):
    c_assert = CustomAssert()

    url = config["env_web"]
    browser.get(url)

    home_page = HomePage(browser)
    home_page.search_a_phone_product()
    c_assert.compare_equal_to(1, 1)
    c_assert.compare_gte(2, 1)
    c_assert.compare_lse_to(1, 2)
