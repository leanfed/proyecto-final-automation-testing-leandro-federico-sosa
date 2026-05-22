@echo off
echo Ejecutando suite completa del Proyecto Final Automation Testing...
if not exist reports mkdir reports
if not exist reports\screenshots mkdir reports\screenshots
if not exist logs mkdir logs

pytest -v --html=reports\reporte.html --self-contained-html

echo.
echo Ejecucion finalizada. Reporte generado en reports\reporte.html
pause
