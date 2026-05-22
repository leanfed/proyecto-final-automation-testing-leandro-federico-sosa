"""Clase base para Page Object Model.

Centraliza acciones repetidas: abrir URL, click, escritura, obtención de texto y esperas.
"""

from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import Config
from utils.logger_config import get_logger


class BasePage:
    """Base común para todas las páginas automatizadas."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = get_logger(self.__class__.__name__)

    def open_url(self, url: str) -> "BasePage":
        self.logger.info("Abriendo URL: %s", url)
        self.driver.get(url)
        return self

    def wait_visible(self, locator: tuple[str, str]) -> WebElement:
        self.logger.info("Esperando visibilidad del elemento: %s", locator)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple[str, str]) -> WebElement:
        self.logger.info("Esperando elemento clickeable: %s", locator)
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_all_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        self.logger.info("Esperando listado de elementos visibles: %s", locator)
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str]) -> "BasePage":
        self.wait_clickable(locator).click()
        return self

    def type_text(self, locator: tuple[str, str], text: str, clear: bool = True) -> "BasePage":
        element = self.wait_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.wait_visible(locator).text.strip()

    def get_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait_all_visible(locator)

    def is_visible(self, locator: tuple[str, str], timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def current_url_contains(self, expected_fragment: str) -> bool:
        return expected_fragment in self.driver.current_url
