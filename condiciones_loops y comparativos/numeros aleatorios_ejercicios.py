# ==========================================
# EJERCICIOS CON RANDOM
# ==========================================

# random sirve para generar valores aleatorios
# Importamos todas las funciones del módulo random
from random import *


# ==========================================
# EJERCICIO 1
# Generar un número entero aleatorio
# ==========================================

# randint(1, 10) genera un número entero aleatorio
# entre 1 y 10, incluyendo ambos números
aleatorio = randint(1, 10)

# Imprimimos el número generado
print(aleatorio)


# ==========================================
# EJERCICIO 2
# Generar un número decimal aleatorio
# ==========================================

# uniform(0, 1) genera un número decimal aleatorio
# entre 0 y 1
# round(..., 1) redondea el número a 1 decimal
aleatorio = round(uniform(0, 1), 1)

# Imprimimos el número decimal generado
print(aleatorio)


# ==========================================
# EJERCICIO 3
# Elegir un elemento aleatorio de una lista
# ==========================================

# Lista de nombres
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

# choice() elige un elemento aleatorio de la lista
sorteo = choice(nombres)

# Imprimimos el nombre seleccionado
print(sorteo)