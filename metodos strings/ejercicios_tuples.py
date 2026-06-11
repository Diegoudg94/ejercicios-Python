# --------------------------------------------------
# EJERCICIO 1
# Objetivo: contar cuántas veces aparece el número 2
# dentro de una tupla.
# --------------------------------------------------

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# count(2) cuenta cuántas veces aparece el valor 2 en la tupla
print(mi_tupla.count(2))


# --------------------------------------------------
# EJERCICIO 2
# Objetivo: convertir una tupla en una lista.
# --------------------------------------------------

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

# list() convierte la tupla en lista
mi_lista = list(mi_tupla)

# type() muestra el tipo de dato de mi_lista
print(type(mi_lista))  # <class 'list'>


# --------------------------------------------------
# EJERCICIO 3
# Objetivo: desempaquetar una tupla en variables.
# --------------------------------------------------

mi_tupla = (1, 2, 3, 4)

# Cada valor de la tupla se guarda en una variable diferente:
# a = 1
# b = 2
# c = 3
# d = 4
a, b, c, d = mi_tupla

# Imprimimos los valores guardados en cada variable
print(a, b, c, d)