"""Factory para crear instancias de WebDriver.

Selenium 4 incluye Selenium Manager, por lo que no hace falta descargar ChromeDriver
manualmente si Chrome está instalado y actualizado.
"""

from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import Config
from utils.logger_config import get_logger


def create_driver() -> webdriver.Chrome:
    """Crea y configura un navegador Chrome para las pruebas UI."""

    logger = get_logger(__name__)

    options = Options()

    if Config.HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # Evita que Chrome interrumpa los tests con avisos de contraseñas guardadas,
    # filtradas o recomendación de cambio de contraseña.
    options.add_argument("--disable-save-password-bubble")
    options.add_argument(
        "--disable-features="
        "PasswordLeakDetection,"
        "PasswordManagerOnboarding,"
        "PasswordGeneration,"
        "AutofillServerCommunication"
    )

    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "safebrowsing.enabled": False,
    }

    options.add_experimental_option("prefs", chrome_prefs)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    driver.maximize_window()

    # Se priorizan esperas explícitas para que cada condición sea clara y mantenible.
    driver.implicitly_wait(0)

    logger.info("Navegador Chrome iniciado. Headless=%s", Config.HEADLESS)

    return driver