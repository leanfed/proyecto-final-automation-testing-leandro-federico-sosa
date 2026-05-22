"""Configuración central del framework de automatización.

El objetivo de este archivo es evitar valores mágicos distribuidos por el proyecto.
Las URLs, tiempos de espera y modo headless se pueden modificar desde un solo lugar.
"""

from __future__ import annotations

import os
from pathlib import Path


class Config:
    """Constantes generales del proyecto."""

    PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]

    SAUCEDEMO_URL: str = os.getenv("SAUCEDEMO_URL", "https://www.saucedemo.com/")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

    EXPLICIT_WAIT: int = int(os.getenv("EXPLICIT_WAIT", "10"))
    PAGE_LOAD_TIMEOUT: int = int(os.getenv("PAGE_LOAD_TIMEOUT", "20"))

    # En GitHub Actions conviene correr en modo headless. En local se puede activar con:
    # Windows: set HEADLESS=true
    # Linux/Mac: export HEADLESS=true
    HEADLESS: bool = (
        os.getenv("HEADLESS", "false").lower() == "true"
        or os.getenv("CI", "false").lower() == "true"
    )

    REPORTS_DIR: Path = PROJECT_ROOT / "reports"
    SCREENSHOTS_DIR: Path = REPORTS_DIR / "screenshots"
    LOGS_DIR: Path = PROJECT_ROOT / "logs"
    DATA_DIR: Path = PROJECT_ROOT / "data"
