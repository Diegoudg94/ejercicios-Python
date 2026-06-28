# metodo open
# open() sirve para abrir un archivo desde Python.
# En este caso estamos abriendo el archivo "prueba.txt".
# Como no indicamos modo, Python lo abre por defecto en modo lectura ("r").

mi_archivo = open("prueba.txt")

# Esto imprime el objeto archivo.
# No muestra el contenido del archivo, solo información técnica:
# nombre, modo de apertura y codificación.
print(mi_archivo)

# type() nos muestra qué tipo de objeto es mi_archivo.
# En este caso es un objeto de tipo TextIOWrapper,
# que representa un archivo de texto abierto.
print(type(mi_archivo))

# read() lee TODO el contenido del archivo completo.
# Si el archivo tiene varias líneas, las lee todas de una sola vez.
print(mi_archivo.read())

# Cerramos el archivo porque ya terminamos de usarlo.
# Es una buena práctica cerrar los archivos después de abrirlos.
mi_archivo.close()


# Volvemos a abrir el archivo.
# Esto es necesario porque después de usar read(),
# el "cursor" del archivo queda al final.
# Si intentáramos leer otra vez sin abrirlo de nuevo,
# ya no habría contenido que leer.
mi_archivo = open("prueba.txt")

print(mi_archivo)
print(type(mi_archivo))

# readline() lee solamente UNA línea del archivo.
# En este caso lee la primera línea.
print(mi_archivo.readline())

mi_archivo.close()


# Abrimos otra vez el archivo para recorrerlo línea por línea.
mi_archivo = open("prueba.txt")

# Un archivo se puede recorrer con un ciclo for.
# Cada vuelta del ciclo toma una línea del archivo.
for l in mi_archivo:
    # l representa cada línea del archivo.
    # El print mostrará el texto "Aqui dice" junto con la línea leída.
    print("Aqui dice ", l)

mi_archivo.close()


# Abrimos nuevamente el archivo para usar readlines().
mi_archivo = open("prueba.txt")

# readlines() lee todas las líneas del archivo,
# pero en lugar de devolver un solo texto,
# devuelve una lista donde cada elemento es una línea.
todas = mi_archivo.readlines()

# pop() elimina y devuelve el último elemento de una lista.
# En este caso estamos sacando la última línea del archivo.
ultima_linea = todas.pop()

# Imprimimos la última línea que sacamos con pop().
print(ultima_linea)

# Cerramos el archivo al final.
mi_archivo.close()