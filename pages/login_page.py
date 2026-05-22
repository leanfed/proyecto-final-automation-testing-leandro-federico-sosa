"""Page Object de la pantalla de login de SauceDemo."""

from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):
    """Acciones y locators de la página de login."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    def open(self) -> "LoginPage":
        self.open_url(Config.SAUCEDEMO_URL)
        self.wait_visible(self.LOGIN_LOGO)
        return self

    def complete_username(self, username: str) -> "LoginPage":
        self.type_text(self.USERNAME_INPUT, username)
        return self

    def complete_password(self, password: str) -> "LoginPage":
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def submit_login(self) -> "LoginPage":
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        self.logger.info("Ejecutando login con usuario: %s", username)
        return self.complete_username(username).complete_password(password).submit_login()

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_page_displayed(self) -> bool:
        return self.is_visible(self.LOGIN_BUTTON)
