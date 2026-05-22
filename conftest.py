"""Configuración global de Pytest.

Incluye:
- fixture de WebDriver
- fixture de logger
- captura automática de screenshots ante fallos
- personalización del reporte HTML
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import pytest

from utils.config import Config
from utils.driver_factory import create_driver
from utils.logger_config import get_logger


def pytest_addoption(parser: pytest.Parser) -> None:
    """Registra opciones personalizadas usadas por el curso en pytest.ini."""

    parser.addini(
        "html_report_title",
        "Título mostrado en el reporte HTML.",
        default="Proyecto Final Automation Testing",
    )
    parser.addini(
        "html_report_description",
        "Descripción mostrada en el reporte HTML.",
        default="Framework de pruebas UI y API con Pytest, Selenium y Requests.",
    )


@pytest.fixture
def logger():
    """Logger disponible para cualquier test."""

    return get_logger("test_execution")


@pytest.fixture
def driver():
    """Crea un WebDriver nuevo por test para mantener independencia entre pruebas."""

    driver_instance = create_driver()
    yield driver_instance
    driver_instance.quit()


def _safe_filename(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_\-]+", "_", value).strip("_")


def _capture_screenshot(driver, test_name: str) -> Path:
    """Guarda screenshot con fecha/hora y nombre del test."""

    Config.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{_safe_filename(test_name)}.png"
    screenshot_path = Config.SCREENSHOTS_DIR / filename
    driver.save_screenshot(str(screenshot_path))
    return screenshot_path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Detecta fallos y adjunta evidencia al reporte HTML cuando existe un navegador."""

    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver_instance = item.funcargs.get("driver")
    if driver_instance is None:
        return

    logger = get_logger("screenshots")
    screenshot_path = _capture_screenshot(driver_instance, item.name)
    logger.error("Test fallido. Screenshot guardado en: %s", screenshot_path)

    # Integración con pytest-html: agrega enlace e imagen al reporte.
    try:
        from pytest_html import extras

        relative_path = screenshot_path.relative_to(Config.PROJECT_ROOT)
        html = (
            f'<div>'
            f'<p><strong>Screenshot de fallo:</strong> {relative_path}</p>'
            f'<a href="{relative_path}" target="_blank">'
            f'<img src="{relative_path}" alt="screenshot" style="width:360px; border:1px solid #ccc;" />'
            f'</a>'
            f'</div>'
        )

        extra = getattr(report, "extras", [])
        extra.append(extras.html(html))
        report.extras = extra
    except Exception as exc:  # pragma: no cover - solo afecta decoración del reporte
        logger.warning("No se pudo adjuntar screenshot al HTML: %s", exc)


def pytest_html_report_title(report):
    """Personaliza el título visual del reporte pytest-html."""

    report.title = "Proyecto Final Automation Testing - Federico Sosa"


def pytest_html_results_summary(prefix, summary, postfix):
    """Agrega una descripción breve al resumen del reporte HTML."""

    prefix.extend(
        [
            "<p><strong>Descripción:</strong> Framework con pruebas UI en SauceDemo, pruebas API en JSONPlaceholder, "
            "Page Object Model, datos externos, logging y screenshots ante fallos.</p>"
        ]
    )
