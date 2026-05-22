#!/usr/bin/env bash
set -e

echo "Ejecutando suite completa del Proyecto Final Automation Testing..."

mkdir -p reports/screenshots
mkdir -p logs

pytest -v --html=reports/reporte.html --self-contained-html

echo "Ejecución finalizada. Reporte generado en reports/reporte.html"
