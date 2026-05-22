"""Pruebas UI sobre SauceDemo usando Selenium WebDriver y Page Object Model."""

from __future__ import annotations

import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json, read_login_users


@pytest.mark.ui
@pytest.mark.login
@pytest.mark.parametrize("username,password,should_login,expected_message", read_login_users())
def test_login_data_driven(driver, logger, username, password, should_login, expected_message):
    """Valida login exitoso y escenarios negativos usando datos externos CSV."""

    logger.info("Inicio test_login_data_driven | usuario=%s | esperado=%s", username, should_login)

    login_page = LoginPage(driver).open()
    login_page.login(username, password)

    if should_login:
        inventory_page = InventoryPage(driver).wait_loaded()

        assert inventory_page.current_url_contains("/inventory.html")
        assert inventory_page.get_title() == "Products"
        assert inventory_page.is_visible(InventoryPage.APP_LOGO)
    else:
        assert login_page.is_login_page_displayed()
        assert expected_message in login_page.get_error_message()


@pytest.mark.ui
@pytest.mark.smoke
def test_catalogo_muestra_productos_y_controles(driver, logger):
    """Verifica que el catálogo cargue con productos visibles y controles principales."""

    logger.info("Inicio test_catalogo_muestra_productos_y_controles")

    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver).wait_loaded()

    first_product_name = inventory_page.get_first_product_name()
    first_product_price = inventory_page.get_first_product_price()

    logger.info("Primer producto listado: %s | %s", first_product_name, first_product_price)

    assert inventory_page.get_title() == "Products"
    assert inventory_page.get_products_count() > 0
    assert first_product_name != ""
    assert first_product_price.startswith("$")
    assert inventory_page.are_main_controls_visible()


@pytest.mark.ui
@pytest.mark.regression
def test_agregar_primer_producto_al_carrito(driver, logger):
    """Agrega el primer producto al carrito y valida que aparezca correctamente."""

    logger.info("Inicio test_agregar_primer_producto_al_carrito")

    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver).wait_loaded()

    product_name, _ = inventory_page.add_first_product_to_cart()

    assert inventory_page.get_cart_badge_text() == "1"

    inventory_page.go_to_cart()
    cart_page = CartPage(driver).wait_loaded()

    assert cart_page.get_title() == "Your Cart"
    assert cart_page.get_items_count() == 1
    assert cart_page.has_product(product_name)


@pytest.mark.ui
@pytest.mark.e2e
def test_checkout_completo_de_un_producto(driver, logger):
    """Ejecuta flujo completo: login, carrito, checkout y confirmación de compra."""

    logger.info("Inicio test_checkout_completo_de_un_producto")

    checkout_data = read_json("checkout_users.json")["valid_customer"]

    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver).wait_loaded()
    product_name, _ = inventory_page.add_first_product_to_cart()

    inventory_page.go_to_cart()
    cart_page = CartPage(driver).wait_loaded()

    assert cart_page.has_product(product_name)

    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(driver).wait_information_page()

    checkout_page.complete_information(
        first_name=checkout_data["first_name"],
        last_name=checkout_data["last_name"],
        postal_code=checkout_data["postal_code"],
    )
    checkout_page.finish_order()

    assert checkout_page.current_url_contains("checkout-complete.html")
    assert checkout_page.get_complete_message() == "Thank you for your order!"
    assert "dispatched" in checkout_page.get_complete_text().lower()


@pytest.mark.ui
@pytest.mark.smoke
def test_logout_regresa_a_login(driver, logger):
    """Valida que el usuario pueda cerrar sesión desde el menú lateral."""

    logger.info("Inicio test_logout_regresa_a_login")

    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver).wait_loaded()

    inventory_page.logout()

    login_page = LoginPage(driver)

    assert login_page.current_url_contains("saucedemo.com")
    assert login_page.is_login_page_displayed()
