from typing import List

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Locator:

    def __init__(self, loc: By.ID, loc_value: str, description: str) -> None:
        self.loc = loc
        self.loc_value = loc_value
        self.description = description

    def get_loc(self) -> By.ID:
        return self.loc

    def get_loc_val(self) -> str:
        return self.loc_value

    def get_loc_desc(self) -> str:
        return self.description

    def get_web_element(self, driver: WebDriver) -> WebElement:
        return driver.find_element(self.loc, self.loc_value)

    def get_web_elements(self, driver: WebDriver) -> list[WebElement]:
        return driver.find_elements(self.loc, self.loc_value)
