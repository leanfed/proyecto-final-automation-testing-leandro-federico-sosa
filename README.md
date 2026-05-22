# Proyecto Final Automation Testing - Federico Sosa

Framework de automatización de pruebas desarrollado como Trabajo Final Integrador del curso de Testing QA Automation.

El proyecto combina pruebas de **UI** con Selenium WebDriver, pruebas de **API** con Requests, estructura con **Page Object Model**, manejo de datos externos, reportes HTML, logging, screenshots automáticos ante fallos y ejecución opcional mediante GitHub Actions.

---

## 1. Propósito del proyecto

El objetivo es demostrar la construcción de un framework de automatización mantenible y escalable, capaz de validar flujos críticos de una aplicación web y endpoints de una API pública.

Sitios utilizados:

- UI: [SauceDemo](https://www.saucedemo.com/)
- API: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

---

## 2. Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- Git y GitHub
- GitHub Actions
- Page Object Model
- CSV y JSON para datos externos
- Logging con `RotatingFileHandler`

---

## 3. Estructura del proyecto

```text
proyecto-final-automation-testing-federico-sosa/
│
├── .github/
│   └── workflows/
│       └── automation-tests.yml
│
├── data/
│   ├── login_users.csv
│   ├── checkout_users.json
│   └── api_posts.json
│
├── docs/
│   ├── casos_de_prueba.md
│   ├── defectos_y_metricas.md
│   ├── guia_commits.md
│   ├── informe_final.md
│   └── plan_de_pruebas.md
│
├── logs/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│   └── screenshots/
│
├── tests/
│   ├── api/
│   │   └── test_jsonplaceholder_api.py
│   └── ui/
│       └── test_saucedemo_ui.py
│
├── utils/
│   ├── config.py
│   ├── data_reader.py
│   ├── driver_factory.py
│   └── logger_config.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_tests.bat
├── run_tests.sh
└── README.md
```

---

## 4. Instalación

### 4.1 Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/proyecto-final-automation-testing-federico-sosa.git
cd proyecto-final-automation-testing-federico-sosa
```

### 4.2 Crear entorno virtual

En Windows CMD:

```bat
python -m venv venv
venv\Scripts\activate.bat
```

En PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación por política de ejecución, usar CMD con `activate.bat`.

En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4.3 Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5. Ejecución de pruebas

### Ejecutar toda la suite

```bash
pytest
```

### Ejecutar solo pruebas UI

```bash
pytest tests/ui -m ui
```

### Ejecutar solo pruebas API

```bash
pytest tests/api -m api
```

### Ejecutar pruebas smoke

```bash
pytest -m smoke
```

### Ejecutar pruebas end-to-end

```bash
pytest -m e2e
```

---

## 6. Generar reporte HTML

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

También se puede ejecutar con el script incluido:

En Windows:

```bat
run_tests.bat
```

En Linux/Mac:

```bash
chmod +x run_tests.sh
./run_tests.sh
```

El reporte quedará disponible en:

```text
reports/reporte.html
```

---

## 7. Evidencias y logs

Cuando una prueba UI falla, el framework genera automáticamente una captura de pantalla en:

```text
reports/screenshots/
```

El log de ejecución queda en:

```text
logs/suite.log
```

El log registra pasos clave, como apertura de navegador, login, navegación, agregado al carrito, checkout y llamadas relevantes.

---

## 8. Casos de prueba incluidos

### UI - SauceDemo

| ID | Caso | Tipo | Resultado esperado |
|---|---|---|---|
| UI-001 | Login data-driven con usuario válido e inválido | Positivo / Negativo | Login exitoso o mensaje de error correcto |
| UI-002 | Validación de catálogo | Smoke | Página Products visible, productos, menú, filtro y carrito presentes |
| UI-003 | Agregar primer producto al carrito | Regresión | Contador incrementa y producto aparece en el carrito |
| UI-004 | Checkout completo | E2E | Compra finalizada con mensaje de confirmación |
| UI-005 | Logout desde menú lateral | Smoke | El usuario regresa al login |

### API - JSONPlaceholder

| ID | Caso | Método | Resultado esperado |
|---|---|---|---|
| API-001 | Obtener post existente | GET | Status 200 y estructura JSON válida |
| API-002 | Obtener post inexistente | GET | Status 404 y cuerpo vacío |
| API-003 | Crear post parametrizado | POST | Status 201 e ID generado |
| API-004 | Eliminar post | DELETE | Status 200 y cuerpo vacío |
| API-005 | Flujo crear, actualizar y eliminar | POST/PATCH/DELETE | Respuestas correctas en cada paso |

---

## 9. Datos externos

El proyecto usa datos externos para evitar hardcodear todos los escenarios:

- `data/login_users.csv`: usuarios válidos e inválidos para login.
- `data/checkout_users.json`: datos del comprador para checkout.
- `data/api_posts.json`: payloads para pruebas API parametrizadas.

---

## 10. Interpretación del reporte

En el reporte HTML se puede revisar:

- cantidad de pruebas ejecutadas;
- estado de cada test: passed, failed, skipped;
- duración de ejecución;
- error detallado en caso de fallo;
- capturas de pantalla asociadas a pruebas UI fallidas.

---

## 11. Integración CI/CD

El workflow de GitHub Actions se encuentra en:

```text
.github/workflows/automation-tests.yml
```

Se ejecuta automáticamente al hacer `push` o `pull request` sobre la rama `main`.

El workflow:

1. instala Python;
2. instala Google Chrome;
3. instala dependencias del proyecto;
4. ejecuta Pytest en modo headless;
5. genera reporte HTML;
6. guarda reportes, logs y screenshots como artefactos.

---

## 12. Buenas prácticas aplicadas

- Separación entre tests y lógica de interacción.
- Page Object Model para mantener locators y acciones centralizados.
- Fixtures de Pytest para crear y cerrar WebDriver.
- Datos externos en CSV y JSON.
- Esperas explícitas con `WebDriverWait`.
- Screenshots automáticos ante fallos.
- Logging rotativo.
- Marcadores para filtrar pruebas (`ui`, `api`, `smoke`, `regression`, `negative`, `e2e`).
- Tests independientes entre sí.

---

## 13. Comandos Git sugeridos

```bash
git init
git add README.md .gitignore requirements.txt pytest.ini
git commit -m "Configura estructura inicial del proyecto"

git add utils/ pages/
git commit -m "Agrega utilidades y Page Object Model"

git add data/
git commit -m "Agrega datos externos para pruebas"

git add tests/ui/
git commit -m "Agrega pruebas UI de SauceDemo"

git add tests/api/
git commit -m "Agrega pruebas API con Requests"

git add conftest.py reports/ logs/
git commit -m "Configura fixtures, reportes, logs y screenshots"

git add .github/workflows/
git commit -m "Agrega workflow de GitHub Actions"

git add docs/
git commit -m "Agrega documentación final del proyecto"
```

---

## 14. Autor

**Leandro Federico Sosa**  
Proyecto Final - QA Automation Testing
