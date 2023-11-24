from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.locators import Locator
import allure

from ui.utils.AllureStepLog import log_step


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 30)

    def get_web_element(self, locator: Locator) -> WebElement:
        return locator.get_web_element(self.driver)

    def click(self, locator: Locator) -> None:
        locator.get_web_element(self.driver).click()
        log_step(f"clicked on {locator.description} using locator {locator.loc_value}")

    def wait_click(self, locator: Locator) -> None:
        self.wait_for_element(locator)
        self.click(locator)
        log_step(f"clicked on {locator.description} using locator {locator.loc_value}")

    def wait_enter(self, locator: Locator, value: str) -> None:
        self.wait_for_element(locator)
        self.enter(locator, value)
        log_step(f"entered {value} on {locator.description} using locator {locator.loc_value}")

    def enter(self, locator: Locator, value: str) -> None:
        locator.get_web_element(self.driver).send_keys(value)
        log_step(f"entered {value} on {locator.description} using locator {locator.loc_value}")

    def wait_for_element(self, locator: Locator) -> None:
        self.wait.until(EC.visibility_of(locator.get_web_element(self.driver)))
        log_step(f"waiting for an element {locator.description} is success")

    def wait_for_element_clickable(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator.get_web_element(self.driver)))
        log_step(f"waiting for an element {locator.description} is success")

    def get_text(self, locator: Locator) -> str:
        self.wait_for_element(locator)
        text = locator.get_web_element(self.driver).text
        log_step(f"element {locator.description} text is {text}")
        return text
