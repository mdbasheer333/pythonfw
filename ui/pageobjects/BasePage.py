import logging

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.locators import Locator
import allure


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 30)
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def get_web_element(self, locator: Locator) -> WebElement:
        return locator.get_web_element(self.driver)

    def click(self, locator: Locator) -> None:
        locator.get_web_element(self.driver).click()
        self.logger.info(f"clicked on {locator.description} using locator {locator.loc_value}")
        with allure.step(f"clicked on {locator.description} using locator {locator.loc_value}"):
            pass

    def wait_click(self, locator: Locator) -> None:
        self.wait_for_element(locator)
        self.click(locator)
        self.logger.info(f"clicked on {locator.description} using locator {locator.loc_value}")
        allure.step(f"clicked on {locator.description} using locator {locator.loc_value}")

    def wait_enter(self, locator: Locator, value: str) -> None:
        self.wait_for_element(locator)
        self.enter(locator, value)
        self.logger.info(f"entered {value} on {locator.description} using locator {locator.loc_value}")
        allure.dynamic.description(f"entered {value} on {locator.description} using locator {locator.loc_value}")

    def enter(self, locator: Locator, value: str) -> None:
        locator.get_web_element(self.driver).send_keys(value)
        self.logger.info(f"entered {value} on {locator.description} using locator {locator.loc_value}")
        allure.dynamic.description(f"entered {value} on {locator.description} using locator {locator.loc_value}")

    def wait_for_element(self, locator: Locator) -> None:
        self.wait.until(EC.visibility_of(locator.get_web_element(self.driver)))

    def wait_for_element_clickable(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator.get_web_element(self.driver)))

    def get_text(self, locator: Locator) -> str:
        self.wait_for_element(locator)
        return locator.get_web_element(self.driver).text
