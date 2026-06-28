# Abrimos o creamos el archivo "prueba1.txt" en modo escritura ("w")
# Si el archivo no existe, Python lo crea
# Si el archivo ya existe, se borra su contenido anterior
archivo = open("prueba1.txt", "w")

# Escribimos la primera línea dentro del archivo
# \n significa "salto de línea", como presionar Enter
archivo.write("Hola\n")

# Escribimos una segunda línea dentro del archivo
archivo.write("Soy una nueva linea\n")

# Cerramos el archivo para guardar correctamente los cambios
archivo.close()