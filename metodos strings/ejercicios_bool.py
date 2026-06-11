# ============================
# EJERCICIO 1
# Comparación de igualdad
# ============================

# En esta operación primero se resuelve la suma: 0 + 1
# Luego se compara si 1 es igual al resultado de esa suma.
prueba = 1 == 0 + 1

# Como 0 + 1 da 1, entonces la comparación es:
# 1 == 1
# Por eso el resultado es True.
print(prueba)


# ============================
# EJERCICIO 2
# Comparación entre operaciones matemáticas
# ============================

# Primero Python resuelve las operaciones matemáticas:
# 17834 / 34
# 87 * 56
#
# Después compara si el resultado de la división
# es mayor que el resultado de la multiplicación.
resultado = 17834 / 34 > 87 * 56

# 17834 / 34 da aproximadamente 524.52
# 87 * 56 da 4872
#
# Como 524.52 no es mayor que 4872,
# el resultado es False.
print(resultado)


# ============================
# EJERCICIO 3
# Potencia y comparación
# ============================

# 25 ** 0.5 calcula la raíz cuadrada de 25.
# Elevar un número a 0.5 es lo mismo que sacar su raíz cuadrada.
#
# Luego se compara si ese resultado es igual a 5.
resultado = (25 ** 0.5) == 5

# Como la raíz cuadrada de 25 es 5,
# la comparación es:
# 5 == 5
# Por eso el resultado es True.
print(resultado)