# Guía de commits graduales

La consigna pide historial de commits que documente el progreso. Esta guía permite subir el proyecto de forma ordenada y creíble.

## Paso 1 - Estructura inicial

```bash
git init
git add README.md .gitignore requirements.txt pytest.ini
git commit -m "Configura estructura inicial del proyecto"
```

## Paso 2 - Utilidades base

```bash
git add utils/
git commit -m "Agrega configuración, lectura de datos, driver factory y logging"
```

## Paso 3 - Page Object Model

```bash
git add pages/
git commit -m "Implementa Page Object Model para SauceDemo"
```

## Paso 4 - Datos externos

```bash
git add data/
git commit -m "Agrega datos externos para pruebas parametrizadas"
```

## Paso 5 - Pruebas UI

```bash
git add tests/ui/
git commit -m "Agrega pruebas UI de login, catálogo, carrito y checkout"
```

## Paso 6 - Pruebas API

```bash
git add tests/api/
git commit -m "Agrega pruebas API con Requests y JSONPlaceholder"
```

## Paso 7 - Fixtures, reportes y evidencias

```bash
git add conftest.py reports/ logs/ run_tests.bat run_tests.sh
git commit -m "Configura fixtures, reportes HTML, logs y screenshots"
```

## Paso 8 - CI/CD

```bash
git add .github/workflows/
git commit -m "Agrega integración continua con GitHub Actions"
```

## Paso 9 - Documentación final

```bash
git add docs/
git commit -m "Agrega documentación final del framework de automatización"
```

## Paso 10 - Conectar con GitHub

```bash
git branch -M main
git remote add origin https://github.com/TU-USUARIO/proyecto-final-automation-testing-federico-sosa.git
git push -u origin main
```
