# Informe Final - Framework de Automatización de Pruebas

**Alumno:** Leandro Federico Sosa  
**Proyecto:** Proyecto Final Automation Testing  
**Repositorio sugerido:** `proyecto-final-automation-testing-federico-sosa`  
**Tecnologías:** Python, Pytest, Selenium WebDriver, Requests, Page Object Model, GitHub Actions

---

## 1. Descripción general

El presente proyecto implementa un framework de automatización de pruebas que cubre pruebas de interfaz web y pruebas de API.

Para la capa UI se utiliza SauceDemo, una aplicación de práctica para testing automatizado. Para la capa API se utiliza JSONPlaceholder, una API pública que permite validar métodos HTTP como GET, POST, PATCH y DELETE.

El framework fue diseñado para ser mantenible, claro y extensible. Para ello se aplicó el patrón Page Object Model, separando los locators y acciones de cada página respecto de las aserciones ubicadas en los tests.

---

## 2. Storytelling del flujo principal

Federico ingresa a SauceDemo como usuario estándar para validar el comportamiento de una tienda demo. Inicia sesión correctamente, revisa el catálogo de productos, identifica el primer producto disponible, lo agrega al carrito y confirma que el contador se actualiza. Luego accede al carrito, verifica que el producto agregado sea el correcto, completa los datos de checkout y finaliza la compra. Al terminar, el sistema muestra el mensaje de confirmación: “Thank you for your order!”.

Este flujo representa una validación end-to-end de una compra simple.

---

## 3. Arquitectura del framework

El framework se organiza en carpetas separadas:

- `pages/`: Page Objects de la aplicación web.
- `tests/ui/`: pruebas de interfaz.
- `tests/api/`: pruebas de API.
- `utils/`: configuración, lectura de datos, driver factory y logging.
- `data/`: datos externos en CSV y JSON.
- `reports/`: reportes HTML y screenshots.
- `logs/`: logs de ejecución.
- `.github/workflows/`: integración con GitHub Actions.
- `docs/`: documentación complementaria.

---

## 4. Pruebas UI implementadas

Se implementaron cinco casos principales de UI:

1. Login data-driven con usuario válido e inválido.
2. Validación del catálogo de productos.
3. Agregado de producto al carrito.
4. Checkout completo.
5. Logout desde el menú lateral.

Estas pruebas cubren escenario positivo, escenario negativo, navegación, carrito y flujo end-to-end.

---

## 5. Pruebas API implementadas

Se implementaron pruebas sobre JSONPlaceholder:

1. GET de recurso existente.
2. GET de recurso inexistente.
3. POST parametrizado con datos externos.
4. DELETE de recurso.
5. Flujo E2E con POST, PATCH y DELETE.

Las validaciones incluyen status code, estructura JSON, tipos de datos, contenido esperado y tiempo de respuesta.

---

## 6. Datos de prueba

El proyecto utiliza datos externos para mejorar mantenimiento y claridad:

- `login_users.csv`: credenciales y resultado esperado.
- `checkout_users.json`: datos del usuario de checkout.
- `api_posts.json`: payloads de API y datos de actualización.

---

## 7. Reportes y evidencias

La suite genera un reporte HTML mediante `pytest-html`. Este reporte muestra:

- tests ejecutados;
- estado de cada test;
- duración;
- detalle de errores;
- evidencia visual cuando hay fallos UI.

Además, los screenshots se guardan automáticamente con nombre descriptivo que incluye fecha, hora y test fallido.

---

## 8. Logging

El sistema de logging registra eventos importantes de la ejecución, tales como:

- inicio del navegador;
- apertura de páginas;
- login;
- acciones sobre productos;
- navegación al carrito;
- checkout;
- ejecución de requests;
- screenshots ante fallos.

El archivo principal es `logs/suite.log`.

---

## 9. CI/CD

Se incluye un workflow opcional de GitHub Actions que ejecuta la suite en cada push o pull request sobre `main`. La ejecución se realiza en modo headless y publica reportes, logs y capturas como artefactos.

---

## 10. Conclusión

El proyecto cumple con los puntos centrales de un framework de automatización: organización clara, pruebas UI y API, Page Object Model, datos externos, reportes, logs, capturas automáticas y CI/CD opcional. La estructura permite incorporar nuevas páginas, nuevos endpoints y nuevos casos de prueba sin modificar la base del framework.
