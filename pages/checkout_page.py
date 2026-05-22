"""Page Object del proceso de checkout de SauceDemo."""

from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Acciones para completar el checkout."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    def wait_information_page(self) -> "CheckoutPage":
        self.wait_visible(self.PAGE_TITLE)
        self.wait_visible(self.FIRST_NAME_INPUT)
        return self

    def complete_information(self, first_name: str, last_name: str, postal_code: str) -> "CheckoutPage":
        self.logger.info("Completando datos de checkout para: %s %s", first_name, last_name)
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_order(self) -> "CheckoutPage":
        self.wait_visible(self.SUMMARY_TOTAL)
        self.click(self.FINISH_BUTTON)
        return self

    def get_complete_message(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self) -> str:
        return self.get_text(self.COMPLETE_TEXT)
