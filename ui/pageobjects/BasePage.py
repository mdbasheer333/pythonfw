from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click(self, locator):
        self.driver.find_element(*locator).click()
        print(f"clicked on {locator}")

    def wait_click(self, locator):
        self.wait_for_element(locator)
        self.click(locator)
        print(f"clicked on {locator}")

    def wait_enter(self, locator, value):
        self.wait_for_element(locator)
        self.enter(locator, value)
        print(f"entered on {locator} with value as {value}")

    def enter(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)
        print(f"entered on {locator} with value as {value}")

    def wait_for_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        print(f"waited for element {locator}")

    def wait_for_element_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        print(f"waited for element {locator}")

    def get_text(self, locator):
        self.wait_for_element(locator)
        txt = self.driver.find_element(*locator).text
        print(f"element {locator} text is {txt}")
        return txt
