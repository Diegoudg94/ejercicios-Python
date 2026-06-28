# Importamos Path desde el módulo pathlib
# pathlib sirve para trabajar con rutas de archivos y carpetas
from pathlib import Path


# Creamos un objeto Path con la ruta del archivo prueba.txt
# Aunque la variable se llama carpeta, en realidad apunta a un archivo
carpeta = Path("/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba.txt")

# read_text() lee todo el contenido del archivo como texto
# Es un método porque lleva paréntesis y realiza una acción
print(carpeta.read_text())



# Volvemos a crear la ruta del archivo
carpeta = Path("/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba.txt")

# name devuelve el nombre completo del archivo, incluyendo su extensión
# En este caso imprimiría: prueba.txt
# Es una propiedad porque NO lleva paréntesis
print(carpeta.name)



# Diferencia entre métodos y propiedades:
#
# Un método realiza una acción y se escribe con paréntesis.
# Ejemplo:
# carpeta.read_text()
#
# Una propiedad solo devuelve información del objeto y se escribe sin paréntesis.
# Ejemplo:
# carpeta.name



# Volvemos a crear la ruta del archivo
carpeta = Path("/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba.txt")

# suffix devuelve la extensión del archivo
# En este caso imprimiría: .txt
# Es una propiedad, por eso no lleva paréntesis
print(carpeta.suffix)



# Volvemos a crear la ruta del archivo
carpeta = Path("/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba.txt")

# stem devuelve el nombre del archivo sin la extensión
# En este caso imprimiría: prueba
# Es una propiedad, por eso no lleva paréntesis
print(carpeta.stem)



# Volvemos a crear la ruta del archivo
carpeta = Path("/Users/diegocovarrubias/Ejercicios Python/Manipulacion archivos/prueba.txt")

# exists() revisa si el archivo o carpeta existe
# Es un método porque realiza una comprobación y lleva paréntesis
#
# exists() devuelve un booleano:
# True  -> si el archivo existe
# False -> si el archivo no existe

# Aquí usamos "not" para negar el resultado booleano
# Si carpeta.exists() es False, entonces not False se convierte en True
if not carpeta.exists():
    print("El archivo no existe")
else:
    print("El archivo existe")