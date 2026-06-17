# ==========================================
# OPERADORES DE COMPARACIÓN EN PYTHON
# ==========================================

# Los operadores de comparación sirven para comparar valores.
# El resultado de una comparación siempre será un booleano:
# True  -> verdadero
# False -> falso

# >   mayor que
# <   menor que
# >=  mayor o igual que
# <=  menor o igual que
# ==  igual que
# !=  diferente que


# ==========================================
# COMPARACIÓN DE STRINGS
# ==========================================

# Creamos una variable con un texto
mi_variable = "Hola mundo"

# Comparamos si el contenido de mi_variable es igual a "Hola mundo"
mi_bool = mi_variable == "Hola mundo"

# Imprimimos el texto original
print(mi_variable)

# Imprimimos el tipo de dato de mi_bool
# En este caso será <class 'bool'>
print(type(mi_bool))

# Imprimimos el resultado de la comparación
# Como ambos textos son iguales, devuelve True
print(mi_bool)


# ==========================================
# COMPARACIÓN DE STRINGS DIFERENTES
# ==========================================

mi_variable = "Hola mundo"

# Comparamos si "Hola mundo" es igual a "Hola python"
# Como son textos diferentes, el resultado será False
mi_bool = mi_variable == "Hola python"

print(mi_variable)
print(type(mi_bool))
print(mi_bool)


# ==========================================
# COMPARACIÓN DE NÚMEROS
# ==========================================

# Comparamos si 10 es igual a 25
# Como no son iguales, devuelve False
mi_bool = 10 == 25
print(mi_bool)


# Python primero resuelve la suma 5 + 5
# Después compara si 10 es igual al resultado de esa suma
# Como 5 + 5 da 10, devuelve True
mi_bool = 10 == 5 + 5
print(mi_bool)


# ==========================================
# COMPARACIÓN DE STRINGS
# ==========================================

# Comparamos si "blanco" es igual a "negro"
# Como son textos diferentes, devuelve False
mi_bool = "blanco" == "negro"
print(mi_bool)


# Python distingue entre mayúsculas y minúsculas.
# "blanco" no sería igual a "Blanco".
# Pero usamos .lower() para convertir "Blanco" a minúsculas.
# Entonces la comparación queda: "blanco" == "blanco"
mi_bool = "blanco" == "Blanco".lower()
print(mi_bool)


# ==========================================
# COMPARACIÓN ENTRE TIPOS DE DATOS
# ==========================================

# Aunque ambos parecen representar el número 100,
# "100" es un string y 100 es un integer.
# Como son tipos de datos diferentes, devuelve False.
mi_bool = "100" == 100
print(mi_bool)


# Aquí comparamos un integer con un float.
# 100 es integer y 100.00 es float.
# Python los reconoce como valores numéricos equivalentes,
# por eso devuelve True.
mi_bool = 100 == 100.00
print(mi_bool)


# ==========================================
# OPERADOR DIFERENTE QUE !=
# ==========================================

# Comparamos si 100 es diferente de 99.
# Como sí son diferentes, devuelve True.
mi_bool = 100 != 99
print(mi_bool)


# ==========================================
# MAYOR QUE Y MENOR QUE
# ==========================================

# Comparamos si 100 es menor que 99.
# Como 100 no es menor que 99, devuelve False.
mi_bool = 100 < 99
print(mi_bool)


# Comparamos si 100 es mayor que 99.
# Como sí lo es, devuelve True.
mi_bool = 100 > 99
print(mi_bool)


# ==========================================
# MAYOR O IGUAL / MENOR O IGUAL
# ==========================================

# Comparamos si 100 es mayor o igual que 99.
# Como 100 es mayor que 99, devuelve True.
mi_bool = 100 >= 99
print(mi_bool)


# Comparamos si 100 es menor o igual que 99.
# Como 100 no es menor ni igual a 99, devuelve False.
mi_bool = 100 <= 99
print(mi_bool)