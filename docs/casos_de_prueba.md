# Casos de Prueba Automatizados

## Casos UI - SauceDemo

| ID | Nombre | Tipo | Datos | Pasos principales | Resultado esperado |
|---|---|---|---|---|---|
| UI-001 | Login data-driven | Positivo/Negativo | `login_users.csv` | Abrir login, ingresar credenciales, enviar formulario | Usuario válido entra a inventario; usuarios inválidos muestran error |
| UI-002 | Catálogo visible | Smoke | Usuario estándar | Login, cargar inventario, leer primer producto | Título Products, productos visibles, controles principales presentes |
| UI-003 | Agregar producto al carrito | Regresión | Usuario estándar | Login, agregar primer producto, ir al carrito | Badge = 1 y producto agregado visible |
| UI-004 | Checkout completo | E2E | `checkout_users.json` | Login, agregar producto, carrito, checkout, finalizar | Mensaje final “Thank you for your order!” |
| UI-005 | Logout | Smoke | Usuario estándar | Login, abrir menú, logout | Regreso a pantalla de login |

## Casos API - JSONPlaceholder

| ID | Endpoint | Método | Tipo | Validaciones |
|---|---|---|---|---|
| API-001 | `/posts/1` | GET | Smoke | Status 200, JSON válido, id entero, title/body no vacíos |
| API-002 | `/posts/999999` | GET | Negativo | Status 404, cuerpo `{}` |
| API-003 | `/posts` | POST | Parametrizado | Status 201, id generado, payload reflejado |
| API-004 | `/posts/1` | DELETE | Regresión | Status 200, cuerpo `{}` |
| API-005 | `/posts` → `/posts/{id}` | POST/PATCH/DELETE | E2E | Creación, actualización parcial y eliminación simulada |
