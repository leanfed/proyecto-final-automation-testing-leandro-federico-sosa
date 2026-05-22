"""Pruebas API con Requests sobre JSONPlaceholder."""

from __future__ import annotations

import pytest
import requests

from utils.config import Config
from utils.data_reader import read_json


@pytest.fixture(scope="module")
def posts_url() -> str:
    """URL base del recurso posts para evitar duplicación en los tests."""

    return f"{Config.API_BASE_URL}/posts"


@pytest.mark.api
@pytest.mark.smoke
def test_get_post_existente_devuelve_estructura_valida(posts_url, logger):
    """GET /posts/1: valida estado, estructura, contenido y tiempo de respuesta."""

    logger.info("Inicio test_get_post_existente_devuelve_estructura_valida")

    response = requests.get(f"{posts_url}/1", timeout=10)
    body = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 2
    assert isinstance(body["id"], int)
    assert body["id"] == 1
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str) and body["title"] != ""
    assert isinstance(body["body"], str) and body["body"] != ""


@pytest.mark.api
@pytest.mark.negative
def test_get_post_inexistente_devuelve_404(posts_url, logger):
    """GET /posts/{id inválido}: valida escenario negativo esperado."""

    logger.info("Inicio test_get_post_inexistente_devuelve_404")

    response = requests.get(f"{posts_url}/999999", timeout=10)

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.api
@pytest.mark.parametrize("payload", read_json("api_posts.json")["posts"])
def test_post_crea_recurso_con_payload_parametrizado(posts_url, logger, payload):
    """POST /posts: valida creación de recurso usando payloads leídos desde JSON."""

    logger.info("Inicio test_post_crea_recurso_con_payload_parametrizado | title=%s", payload["title"])

    response = requests.post(posts_url, json=payload, timeout=10)
    body = response.json()

    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 2
    assert isinstance(body["id"], int)
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]


@pytest.mark.api
@pytest.mark.regression
def test_delete_post_devuelve_respuesta_exitosa(posts_url, logger):
    """DELETE /posts/1: valida borrado simulado exitoso en JSONPlaceholder."""

    logger.info("Inicio test_delete_post_devuelve_respuesta_exitosa")

    response = requests.delete(f"{posts_url}/1", timeout=10)

    assert response.status_code == 200
    assert response.json() == {}


@pytest.mark.api
@pytest.mark.e2e
def test_flujo_api_crear_actualizar_y_eliminar_recurso(posts_url, logger):
    """Flujo API e2e: POST -> PATCH -> DELETE.

    JSONPlaceholder simula las operaciones, por lo que se validan las respuestas
    de cada paso sin asumir persistencia real en el servidor.
    """

    logger.info("Inicio test_flujo_api_crear_actualizar_y_eliminar_recurso")

    test_data = read_json("api_posts.json")
    payload = test_data["posts"][0]
    patch_data = test_data["patch_update"]

    create_response = requests.post(posts_url, json=payload, timeout=10)
    created_body = create_response.json()

    assert create_response.status_code == 201
    assert "id" in created_body

    resource_id = created_body["id"]

    update_response = requests.patch(f"{posts_url}/{resource_id}", json=patch_data, timeout=10)
    updated_body = update_response.json()

    assert update_response.status_code == 200
    assert updated_body["title"] == patch_data["title"]

    delete_response = requests.delete(f"{posts_url}/{resource_id}", timeout=10)

    assert delete_response.status_code == 200
    assert delete_response.json() == {}
