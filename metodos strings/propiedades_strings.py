# PROPIEDADES DE LOS STRINGS

# Los strings son cadenas de texto.
# En Python, los strings tienen varias propiedades:
# - Son inmutables: no se puede cambiar una letra directamente dentro del texto.
# - Se pueden concatenar: unir textos con +
# - Se pueden multiplicar: repetir textos con *
# - Pueden tener varias líneas.
# - Podemos verificar si contienen una palabra.
# - Podemos calcular su longitud con len()


# -------------------------------------------------
# 1. Multiplicar strings
# -------------------------------------------------

# Creamos un string con el texto "ka"
n1 = "ka"

# Al multiplicarlo por 9, Python repite el texto 9 veces
print(n1 * 9)  # kakakakakakakakaka


# -------------------------------------------------
# 2. String con salto de línea usando \n
# -------------------------------------------------

# \n sirve para hacer un salto de línea dentro del texto
poema = "Mil pequeños peces blancos \ncomo si hirviera el color del agua"

print(poema)


# -------------------------------------------------
# 3. String de varias líneas usando triple comilla
# -------------------------------------------------

# Las triple comillas """ """ permiten escribir texto en varias líneas
poema = """Mil pequeños peces blancos
como si hirviera el color del agua"""

print(poema)


# -------------------------------------------------
# 4. Verificar si una palabra está dentro del string
# -------------------------------------------------

# "agua" in poema pregunta si la palabra "agua" existe dentro del texto.
# Devuelve True si existe y False si no existe.
print("agua" in poema)  # True


# -------------------------------------------------
# 5. Verificar si una palabra NO está dentro del string
# -------------------------------------------------

# "sol" not in poema pregunta si la palabra "sol" NO existe dentro del texto.
# Devuelve True porque "sol" no aparece en el poema.
print("sol" not in poema)  # True


# -------------------------------------------------
# 6. Calcular la longitud del string
# -------------------------------------------------

# len(poema) cuenta cuántos caracteres tiene el texto.
# Cuenta letras, espacios y saltos de línea.
print(len(poema))