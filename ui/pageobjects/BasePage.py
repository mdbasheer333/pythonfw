from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.locators import Locator


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 30)

    def get_web_element(self, locator: Locator) -> WebElement:
        return locator.get_web_element(self.driver)

    def click(self, locator: Locator) -> None:
        locator.get_web_element(self.driver).click()
        print(f"clicked on {locator.description} using locator {locator.loc_value}")

    def wait_click(self, locator: Locator) -> None:
        self.wait_for_element(locator)
        self.click(locator)
        print(f"clicked on {locator.description} using locator {locator.loc_value}")

    def wait_enter(self, locator: Locator, value: str) -> None:
        self.wait_for_element(locator)
        self.enter(locator, value)
        print(f"entered {value} on {locator.description} using locator {locator.loc_value}")

    def enter(self, locator: Locator, value: str) -> None:
        locator.get_web_element(self.driver).send_keys(value)
        print(f"entered {value} on {locator.description} using locator {locator.loc_value}")

    def wait_for_element(self, locator: Locator) -> None:
        self.wait.until(EC.visibility_of(locator.get_web_element(self.driver)))

    def wait_for_element_clickable(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator.get_web_element(self.driver)))

    def get_text(self, locator: Locator) -> str:
        self.wait_for_element(locator)
        return locator.get_web_element(self.driver).text
