# Importamos el módulo os
# Este módulo nos permite trabajar con carpetas, rutas y archivos del sistema operativo
import os


# os.getcwd() obtiene la ruta actual desde donde se está ejecutando el programa
ruta = os.getcwd()

# Imprimimos la ruta actual
print(ruta)



# Importamos nuevamente os
# En este caso no sería necesario repetirlo porque ya lo importamos arriba,
# pero no genera error
import os


# os.chdir() cambia la carpeta actual de trabajo
# A partir de aquí, Python buscará archivos dentro de esta ruta
os.chdir("/Users/diegocovarrubias/prueba")


# Abrimos el archivo llamado "otro archivo.txt"
# Como ya cambiamos la carpeta con os.chdir(),
# Python buscará este archivo dentro de "/Users/diegocovarrubias/prueba"
archivo = open("otro archivo.txt")


# Leemos e imprimimos todo el contenido del archivo
print(archivo.read())


# Cerramos el archivo para liberar memoria y evitar errores
archivo.close()



# os.makedirs() crea una carpeta nueva
# En este caso crea la carpeta "otra" dentro de "/Users/diegocovarrubias/prueba"
os.makedirs("/Users/diegocovarrubias/prueba/otra")



# Guardamos una ruta completa en una variable
ruta = '/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba.txt'


# os.path.basename() extrae solamente el nombre del archivo de una ruta completa
# En este caso obtiene "prueba.txt"
archivo = os.path.basename(ruta)


# Imprimimos el nombre del archivo
print(archivo)



# os.path.split() separa la ruta en dos partes:
# 1. La carpeta donde está el archivo
# 2. El nombre del archivo
mi_ruta = os.path.split(ruta)


# Imprimimos la ruta separada en una tupla
print(mi_ruta)



# os.rmdir() elimina una carpeta vacía
# En este caso elimina la carpeta "otra"
# Importante: si la carpeta tiene archivos dentro, dará error
os.rmdir("/Users/diegocovarrubias/prueba/otra")



# Importamos Path desde pathlib
# pathlib es una forma más moderna y cómoda de trabajar con rutas
from pathlib import Path


# Creamos una ruta usando Path
# Esta ruta apunta a la carpeta "prueba"
carpeta = Path("/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba")


# Usamos / para unir la carpeta con el nombre del archivo
# Esto crea la ruta completa hacia "otro archivo.txt"
archivo = carpeta / "otro archivo.txt"


# Imprimimos la ruta completa del archivo
print(archivo)