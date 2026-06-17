# ==========================================
# EJERCICIO 1
# Comparación con mayor o igual que >=
# ==========================================

# Creamos dos variables numéricas
num1 = 36
num2 = 17

# Comparamos si num1 es mayor o igual que num2
# En este caso: 36 >= 17
# Como 36 sí es mayor que 17, el resultado será True
mi_bool = num1 >= num2

print(mi_bool)


# ==========================================
# EJERCICIO 2
# Comparación de igualdad ==
# ==========================================

# Calculamos la raíz cuadrada de 25
# Elevar un número a 0.5 es lo mismo que sacar su raíz cuadrada
num1 = 25 ** 0.5

# Guardamos el número 5 en otra variable
num2 = 5

# Comparamos si num1 es igual a num2
# En este caso: 5.0 == 5
# Aunque uno es float y el otro integer, Python los reconoce como valores equivalentes
mi_bool = num1 == num2

print(mi_bool)


# ==========================================
# EJERCICIO 3
# Comparación con diferente que !=
# ==========================================

# Primero Python resuelve las multiplicaciones
num1 = 64 * 3
num2 = 24 * 8

# 64 * 3 da 192
# 24 * 8 también da 192
#
# Después comparamos si num1 es diferente de num2
# En este caso: 192 != 192
# Como no son diferentes, el resultado será False
mi_bool = num1 != num2

print(mi_bool)