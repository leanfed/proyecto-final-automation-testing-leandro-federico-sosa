# Plan de Pruebas - Proyecto Final Automation Testing

## 1. Alcance

El framework valida dos capas principales:

1. **Interfaz Web (UI)** sobre SauceDemo.
2. **API REST** sobre JSONPlaceholder.

## 2. Objetivos

- Validar flujos críticos de usuario.
- Confirmar respuestas esperadas de endpoints públicos.
- Detectar errores funcionales mediante aserciones claras.
- Generar evidencia mediante reporte HTML, logs y screenshots.
- Mantener los tests independientes entre sí.

## 3. Estrategia de pruebas

### UI

- Automatización con Selenium WebDriver.
- Page Object Model para separar interacción y validación.
- Esperas explícitas para reducir falsos negativos.
- Datos externos CSV/JSON.
- Screenshots automáticos ante fallos.

### API

- Requests para consumo de endpoints.
- Validación de status code.
- Validación de estructura y contenido JSON.
- Validación de tiempo de respuesta.
- Parametrización con datos externos.

## 4. Entornos

| Elemento | Valor |
|---|---|
| Lenguaje | Python |
| Framework | Pytest |
| Navegador principal | Google Chrome |
| UI target | https://www.saucedemo.com/ |
| API target | https://jsonplaceholder.typicode.com/ |
| Sistema local sugerido | Windows / Linux / Mac |
| CI/CD | GitHub Actions |

## 5. Criterios de entrada

- Python instalado.
- Dependencias instaladas desde `requirements.txt`.
- Acceso a internet.
- Chrome instalado para pruebas UI.
- Repositorio clonado localmente.

## 6. Criterios de salida

- Pruebas ejecutadas con Pytest.
- Reporte HTML generado.
- Logs disponibles.
- Screenshots generados en caso de fallos.
- Evidencia lista para adjuntar en la entrega.

## 7. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Cambio en locators de SauceDemo | Fallo de tests UI | Locators centralizados en Page Objects |
| Lentitud de red | Fallos por timeout | Uso de timeout y esperas explícitas |
| API pública no disponible | Fallos API | Reintento manual y revisión de status |
| Diferencias entre local y CI | Fallos en GitHub Actions | Ejecución headless configurada por variable |
