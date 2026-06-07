# Guia para hacer commits en git #

1. git status # revisa que archivos cambiaron 
 Este comando muestra:

Archivos nuevos
Archivos modificados
Archivos eliminados
Archivos que aún no están agregados al commit

2 . git add . # preparacion para subir el archivo

Para agregar solo un archivo específico: git add nombre_del_archivo.py

3. Crear el commit 
Despues de agrevar el archivo se crea el commit 
git commit -m "mensaje del cambio"

4. subir cambios git push


Flujo completo 

git status
git diff
git add .
git commit -m "describe el cambio"
git push

// 

git diff revisa que cambios hay entre la ultima version y la actual
