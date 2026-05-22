"""Page Object de la página de inventario/productos."""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Acciones y validaciones básicas del catálogo de productos."""

    APP_LOGO = (By.CLASS_NAME, "app_logo")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    FIRST_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def wait_loaded(self) -> "InventoryPage":
        self.wait_visible(self.APP_LOGO)
        self.wait_visible(self.PAGE_TITLE)
        self.wait_all_visible(self.PRODUCT_CARDS)
        return self

    def get_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_products_count(self) -> int:
        return len(self.get_elements(self.PRODUCT_CARDS))

    def get_first_product_name(self) -> str:
        return self.get_elements(self.PRODUCT_NAMES)[0].text.strip()

    def get_first_product_price(self) -> str:
        return self.get_elements(self.PRODUCT_PRICES)[0].text.strip()

    def add_first_product_to_cart(self) -> tuple[str, str]:
        product_name = self.get_first_product_name()
        product_price = self.get_first_product_price()

        self.logger.info("Agregando primer producto al carrito: %s | %s", product_name, product_price)
        self.click(self.FIRST_ADD_TO_CART_BUTTON)
        self.wait_visible(self.CART_BADGE)

        return product_name, product_price

    def get_cart_badge_text(self) -> str:
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self) -> "InventoryPage":
        self.click(self.CART_LINK)
        return self

    def open_menu(self) -> "InventoryPage":
        self.click(self.MENU_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        return self

    def logout(self) -> "InventoryPage":
        """Cierra sesión y espera explícitamente el regreso a la pantalla de login."""
        self.open_menu()
        self.click(self.LOGOUT_LINK)

        # Evita que el test valide la pantalla de login antes de que termine la redirección.
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))

        return self

    def are_main_controls_visible(self) -> bool:
        return (
            self.is_visible(self.MENU_BUTTON)
            and self.is_visible(self.PRODUCT_SORT)
            and self.is_visible(self.CART_LINK)
        )