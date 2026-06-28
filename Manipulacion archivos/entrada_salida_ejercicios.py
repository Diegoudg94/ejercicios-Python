# Ejercicio 1: leer e imprimir la segunda línea del archivo

# Abrimos el archivo "texto.txt" en modo lectura.
# Como no escribimos ningún modo, Python usa por defecto "r" de read.
mi_archivo = open("texto.txt")

# readline() lee una línea del archivo.
# Aquí leemos la primera línea, pero no la imprimimos.
# Esto sirve para "saltar" la primera línea.
mi_archivo.readline()

# Volvemos a usar readline().
# Como la primera línea ya fue leída, ahora Python lee la segunda línea.
# Esta vez sí la imprimimos.
print(mi_archivo.readline())

# Cerramos el archivo después de usarlo.
mi_archivo.close()


# Ejercicio 2: leer e imprimir solo la primera línea del archivo

# Abrimos nuevamente el archivo.
# Lo abrimos otra vez porque en el ejercicio anterior ya lo habíamos cerrado.
mi_archivo = open("texto.txt")

# readline() lee solamente una línea.
# Como acabamos de abrir el archivo, empieza desde el inicio,
# por eso imprime la primera línea.
print(mi_archivo.readline())

# Cerramos el archivo.
mi_archivo.close()


# Ejercicio 3: leer e imprimir todo el contenido del archivo

# Abrimos nuevamente el archivo.
mi_archivo = open("texto.txt")

# read() lee todo el contenido del archivo completo.
# A diferencia de readline(), no lee solo una línea,
# sino todo el texto de principio a fin.
print(mi_archivo.read())

# Cerramos el archivo al terminar.
mi_archivo.close()