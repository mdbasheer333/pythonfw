import pytest

from ui.pageobjects.HomePage import HomePage
import os

from ui.utils.CustomAssert import CustomAssert


class TestSearch:

    @pytest.mark.smoke
    def test_search(self, browser):
        c_assert = CustomAssert()

        url = os.getenv("env_web")
        browser.get(url)

        home_page = HomePage(browser)
        home_page.search_a_phone_product()
        c_assert.compare_equal_to(1, 1)
        c_assert.compare_gte(2, 1)
        c_assert.compare_lse_to(1, 2)

