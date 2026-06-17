# ==========================================
# APUNTES: MÓDULO RANDOM
# ==========================================

# random es una librería de Python que sirve para trabajar con valores aleatorios
# Para usar sus funciones, primero debemos importarlas


# ==========================================
# randint()
# Genera números enteros aleatorios
# ==========================================

# Importamos solo la función randint
from random import randint

# randint(10, 20) genera un número entero entre 10 y 20
# Incluye el 10 y también el 20
aleatorio = randint(10, 20)

print(aleatorio)


# ==========================================
# Importar varias funciones
# ==========================================

# Podemos importar varias funciones separándolas con coma
from random import randint, uniform

# randint genera un número entero aleatorio
aleatorio = randint(10, 20)

print(aleatorio)


# ==========================================
# uniform()
# Genera números decimales aleatorios
# ==========================================

from random import randint, uniform

# uniform(1, 5) genera un número decimal entre 1 y 5
aleatorio = uniform(1, 5)

print(aleatorio)


# ==========================================
# round() con uniform()
# ==========================================

# Importamos todas las funciones del módulo random
from random import *

# uniform(1, 5) genera un decimal
# round(..., 1) lo redondea a 1 decimal
aleatorio = round(uniform(1, 5), 1)

print(aleatorio)


# ==========================================
# random()
# ==========================================

# random() genera un número decimal aleatorio entre 0 y 1
aleatorio = random()

print(aleatorio)


# ==========================================
# choice()
# Elegir un elemento aleatorio de una lista
# ==========================================

# Lista de colores
colores = ["rojo", "verde", "azul"]

# choice() elige un elemento aleatorio de la lista
aleatorio = choice(colores)

print(aleatorio)


# ==========================================
# shuffle()
# Mezclar elementos de una lista
# ==========================================

# Creamos una lista con números del 5 al 45, avanzando de 5 en 5
numeros = list(range(5, 50, 5))

# shuffle() mezcla los elementos de la lista
# OJO: modifica la lista original
shuffle(numeros)

print(numeros)


# ==========================================
# shuffle() con strings en una lista
# ==========================================

# Lista de colores
colores = ["rojo", "verde", "azul"]

# Mezclamos el orden de los colores
shuffle(colores)

print(colores)