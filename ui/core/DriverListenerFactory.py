from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support.events import EventFiringWebDriver

from ui.utils import logger, allurelog


class WebDriverListener(AbstractEventListener):

    def __init__(self):
        self.logger = logger.logger

    def before_navigate_to(self, url: str, driver) -> None:
        pass

    def after_navigate_to(self, url: str, driver) -> None:
        self.logger.info(f"navigated to {url}")
        allurelog.log_step(f"navigated to {url}")

    def before_navigate_back(self, driver) -> None:
        pass

    def after_navigate_back(self, driver) -> None:
        pass

    def before_navigate_forward(self, driver) -> None:
        pass

    def after_navigate_forward(self, driver) -> None:
        pass

    def before_find(self, by, value, driver) -> None:
        pass

    def after_find(self, by, value, driver) -> None:
        pass

    def before_click(self, element, driver) -> None:
        pass

    def after_click(self, element, driver) -> None:
        pass

    def before_change_value_of(self, element, driver) -> None:
        pass

    def after_change_value_of(self, element, driver) -> None:
        pass

    def before_execute_script(self, script, driver) -> None:
        pass

    def after_execute_script(self, script, driver) -> None:
        pass

    def before_close(self, driver) -> None:
        pass

    def after_close(self, driver) -> None:
        self.logger.info(f"browser closed....!")
        allurelog.log_step(f"browser closed....!")

    def before_quit(self, driver) -> None:
        pass

    def after_quit(self, driver) -> None:
        self.logger.info(f"browser quit....!")
        allurelog.log_step(f"browser quit....!")

    def on_exception(self, exception: Exception, driver) -> None:
        self.logger.error(exception.__dict__)
        allurelog.log_step(exception.__dict__)


class DriverFactory:

    @staticmethod
    def get_driver(browser_type) -> EventFiringWebDriver:
        if browser_type == "chrome" or browser_type == "gc":
            service = Service()
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(service=service, options=options)
        elif browser_type == "ff" or browser_type == "firefox":
            driver = webdriver.Firefox()
        elif browser_type == "edge":
            driver = webdriver.Edge()
        elif browser_type == "remote-chrome" or browser_type == "rc":
            driver = webdriver.Remote(
                command_executor="http://10.0.0.10:4444")
        else:
            allurelog.log_step(f"given wrong browser name {browser_type}")
            logger.logger.critical(f"given wrong browser name {browser_type}")
            raise Exception("given wrong browser name ", browser_type)
        driver.maximize_window()
        driver = EventFiringWebDriver(driver, WebDriverListener())

        return driver
