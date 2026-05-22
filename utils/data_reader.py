"""Lectura de datos externos para pruebas data-driven."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from utils.config import Config


def _as_bool(value: str) -> bool:
    """Convierte valores de CSV a booleano de manera segura."""

    return str(value).strip().lower() in {"true", "1", "yes", "si", "sí"}


def read_login_users() -> list[tuple[str, str, bool, str]]:
    """Lee credenciales desde CSV para parametrizar tests de login UI."""

    path = Config.DATA_DIR / "login_users.csv"
    rows: list[tuple[str, str, bool, str]] = []

    with path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(
                (
                    row["username"],
                    row["password"],
                    _as_bool(row["should_login"]),
                    row.get("expected_message", ""),
                )
            )

    return rows


def read_json(filename: str) -> dict[str, Any]:
    """Lee un archivo JSON ubicado dentro de la carpeta data/."""

    path: Path = Config.DATA_DIR / filename
    with path.open(encoding="utf-8") as json_file:
        return json.load(json_file)
