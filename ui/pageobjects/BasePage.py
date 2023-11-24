from typing import List, Dict, Any, Optional

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ui.locators.locators import Locator
from ui.utils import logger


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.timeout = 60
        self.wait: WebDriverWait = WebDriverWait(self.driver, self.timeout)
        self.logger = logger.logger

    def get_web_element(self, locator: Locator) -> WebElement:
        return locator.get_web_element(self.driver)

    def get_web_elements(self, locator: Locator) -> list[WebElement]:
        return locator.get_web_elements(self.driver)

    def click(self, locator: Locator) -> None:
        locator.get_web_element(self.driver).click()
        self.logger.info(f"clicked on '{locator.description}' using locator '{locator.loc_value}'")

    def wait_click(self, locator: Locator) -> None:
        self.wait_for_element(locator)
        self.click(locator)
        self.logger.info(f"clicked on '{locator.description}' using locator '{locator.loc_value}'")

    def js_click_element(self, locator: Locator) -> None:
        try:
            self.driver.execute_script("arguments[0].click();", locator.get_web_element(self.driver))
        except Exception as e:
            self.logger.error(f"JavaScript click failed:  {e} for locator '{locator.description}'")
            raise Exception(f"JavaScript click failed:  {e} for locator '{locator.description}'")

    def wait_enter(self, locator: Locator, value: str) -> None:
        self.wait_for_element(locator)
        self.enter(locator, value)
        self.logger.info(f"entered '{value}' on '{locator.description}' using locator '{locator.loc_value}'")

    def enter(self, locator: Locator, value: str) -> None:
        locator.get_web_element(self.driver).send_keys(value)
        self.logger.info(f"entered '{value}' on '{locator.description}' using locator '{locator.loc_value}'")

    def is_element_present(self, locator: Locator) -> bool:
        try:
            return locator.get_web_element(self.driver).is_displayed()
        except NoSuchElementException:
            return False

    def is_element_displayed(self, locator: Locator) -> bool:
        return locator.get_web_element(self.driver).is_displayed()

    def wait_for_element(self, locator: Locator) -> None:
        self.wait.until(EC.visibility_of(locator.get_web_element(self.driver)))
        self.logger.info(f"element '{locator.description}' found")

    def wait_for_element_clickable(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator.get_web_element(self.driver)))
        self.logger.info(f"element '{locator.description}' found and clickable")

    def get_text(self, locator: Locator) -> str:
        return locator.get_web_element(self.driver).text

    def get_attribute(self, locator: Locator, attributeName: str) -> str:
        return locator.get_web_element(self.driver).get_attribute(attributeName)

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    def switch_to_frame(self, frame_reference) -> None:
        self.driver.switch_to.frame(frame_reference)

    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    def switch_to_window_by_title(self, title: str) -> str:
        current_window_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title in self.driver.title:
                self.logger.info(f"Window with title '{title}' found.")
                return handle
        self.driver.switch_to.window(current_window_handle)
        self.logger.error(f"Window with title '{title}' not found.")
        raise Exception(f"Window with title '{title}' not found.")

    def move_to_element(self, locator: Locator) -> None:
        ActionChains(self.driver).move_to_element(locator.get_web_element(self.driver)).perform()
        self.logger.info(f"moved to element '{locator.description}'")

    def select_dropdown_by_visible_text(self, locator: Locator, text: str) -> None:
        try:
            from selenium.webdriver.support.ui import Select
            select = Select(locator.get_web_element(self.driver))
            select.select_by_visible_text(text)
        except Exception as e:
            self.logger.error(f"Selection by visible text '{text}' failed for '{locator.description}', reason is {e}")
            raise Exception(f"Selection by visible text '{text}' failed for '{locator.description}', reason is {e}")

    def get_dropdown_options(self, locator: Locator) -> List[str]:
        try:
            from selenium.webdriver.support.ui import Select
            select = Select(locator.get_web_element(self.driver))
            vals = [option.text for option in select.options]
            self.logger.info(f"values of '{locator.description}' are {vals}")
            return vals
        except Exception as e:
            self.logger.error(f"Failed to retrieve '{locator.description}' dropdown options: {e}")
            raise Exception(f"Failed to retrieve '{locator.description}' dropdown options: {e}")

    def get_selected_option(self, locator: Locator) -> str:
        try:
            from selenium.webdriver.support.ui import Select
            select = Select(locator.get_web_element(self.driver))
            return select.first_selected_option.text
        except Exception as e:
            self.logger.error(f"Failed to retrieve '{locator.description}' dropdown options: {e}")
            raise Exception(f"Failed to retrieve '{locator.description}' dropdown options: {e}")

    def wait_for_page_load(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except Exception as e:
            self.logger.error(f"Page load timeout: {e}")

    def get_table_rows(self, table_element: Locator) -> List[WebElement]:
        try:
            rows = table_element.get_web_element(self.driver).find_elements(By.TAG_NAME, "tr")
            return rows
        except Exception as e:
            self.logger.warning(f"Failed to retrieve table rows: {e}")
            return []

    def get_table_columns(self, row_element: WebElement) -> List[WebElement]:
        try:
            columns = row_element.find_elements(By.TAG_NAME, "td")
            return columns
        except Exception as e:
            self.logger.warning(f"Failed to retrieve table columns: {e}")
            return []

    def get_cell_text(self, cell_element: WebElement) -> Optional[str]:
        try:
            return cell_element.text
        except Exception as e:
            self.logger.warning(f"Failed to retrieve cell text: {e}")
            return None

    def get_table_values_as_list_of_dicts(self, table_element: Locator) -> List[Dict[str, Any]]:
        try:
            rows = self.get_table_rows(table_element)
            headers = [header.text for header in self.get_table_columns(rows[0])]
            table_values = []
            for row in rows[1:]:  # Skip the header row
                row_data = {}
                columns = self.get_table_columns(row)
                for index, column in enumerate(columns):
                    row_data[headers[index]] = self.get_cell_text(column)
                table_values.append(row_data)
            return table_values
        except Exception as e:
            self.logger.warning(f"Failed to retrieve table '{table_element.description}' values: {e}")
            return []

    def get_cell_value(self, table_element: Locator, row_num: int, col_num: int) -> Optional[str]:
        try:
            rows = self.get_table_rows(table_element)
            columns = self.get_table_columns(rows[row_num - 1])  # Adjust row_num to 0-based index
            cell_text = self.get_cell_text(columns[col_num - 1])  # Adjust col_num to 0-based index
            return cell_text
        except Exception as e:
            self.logger.warning(f"Failed to retrieve cell value: {e} for '{table_element.description}'")
            return None

    def close(self) -> None:
        self.driver.close()

    def quit(self) -> None:
        self.driver.quit()
