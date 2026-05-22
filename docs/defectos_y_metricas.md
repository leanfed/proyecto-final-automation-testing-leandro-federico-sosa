# Defectos, Métricas y Cobertura

## 1. Gestión de defectos

Cuando un test falla, el framework permite registrar evidencia objetiva:

- nombre del test;
- fecha y hora;
- screenshot automático si es una prueba UI;
- log de ejecución;
- stack trace en el reporte HTML;
- endpoint o pantalla afectada.

## 2. Ciclo de vida sugerido para un bug

1. **Nuevo:** se detecta el fallo durante la ejecución automatizada.
2. **Asignado:** se asigna al responsable técnico.
3. **En progreso:** el desarrollador analiza causa raíz.
4. **Resuelto:** se aplica corrección.
5. **Verificado:** QA vuelve a ejecutar el test asociado.
6. **Cerrado:** se confirma que el comportamiento esperado fue restaurado.

## 3. Métricas principales

| Métrica | Cómo se obtiene | Objetivo |
|---|---|---|
| Total de tests ejecutados | Reporte HTML | 100% de suite ejecutada |
| Tests pasados | Reporte HTML | Mayoría de casos en verde |
| Tests fallidos | Reporte HTML | Analizar causa raíz |
| Duración | Reporte HTML | Detectar lentitud |
| Screenshots de fallos | `reports/screenshots/` | Evidencia visual |
| Logs | `logs/suite.log` | Depuración técnica |

## 4. Cobertura funcional

| Área | Cobertura |
|---|---|
| Login | Usuario válido, bloqueado e inválido |
| Catálogo | Productos, título, controles principales |
| Carrito | Agregado y validación de producto |
| Checkout | Flujo completo de compra |
| Logout | Cierre de sesión |
| API GET | Recurso existente e inexistente |
| API POST | Creación parametrizada |
| API DELETE | Eliminación simulada |
| API E2E | POST → PATCH → DELETE |

## 5. Mejoras futuras

- Agregar ejecución cross-browser.
- Agregar pruebas mobile/responsive.
- Incluir Allure Report como alternativa visual.
- Separar ambientes por archivo `.env`.
- Agregar retry controlado para fallos intermitentes de red.
