"""Configuración de logging del framework.

Se utiliza RotatingFileHandler para evitar que el archivo de log crezca sin límite.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from utils.config import Config


def get_logger(name: str = "automation_framework") -> logging.Logger:
    """Devuelve un logger reutilizable para tests, páginas y utilidades."""

    Config.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        Config.LOGS_DIR / "suite.log",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
