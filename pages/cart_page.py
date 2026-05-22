"""Page Object del carrito de compras."""

from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """Acciones y consultas sobre el carrito."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def wait_loaded(self) -> "CartPage":
        self.wait_visible(self.PAGE_TITLE)
        return self

    def get_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_items_count(self) -> int:
        if not self.is_visible(self.CART_ITEMS, timeout=2):
            return 0
        return len(self.get_elements(self.CART_ITEMS))

    def get_product_names(self) -> list[str]:
        return [element.text.strip() for element in self.get_elements(self.CART_ITEM_NAMES)]

    def has_product(self, expected_name: str) -> bool:
        return expected_name in self.get_product_names()

    def go_to_checkout(self) -> "CartPage":
        self.click(self.CHECKOUT_BUTTON)
        return self
