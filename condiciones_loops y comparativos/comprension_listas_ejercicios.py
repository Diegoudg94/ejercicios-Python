# ==========================================
# EJERCICIO 1
# Elevar cada valor al cuadrado
# ==========================================

# Lista original de números
valores = [1, 2, 3, 4, 5, 6, 9.5]

# Creamos una nueva lista donde cada número se eleva al cuadrado
# v**2 significa: v elevado a la potencia 2
# Ejemplo:
# 2**2 = 4
# 3**2 = 9
# 9.5**2 = 90.25
valores_cuadrados = [v**2 for v in valores]

# Imprimimos la lista con los cuadrados
print(valores_cuadrados)


# ==========================================
# EJERCICIO 2
# Obtener solo los números pares
# ==========================================

# Lista original de números
valores = [1, 2, 3, 4, 5, 6, 9.5]

# Creamos una nueva lista solo con los valores pares
# El operador % obtiene el residuo de una división
# Si v % 2 == 0, significa que el número se divide entre 2 exacto
#
# Ejemplo:
# 4 % 2 = 0  -> es par
# 5 % 2 = 1  -> no es par
# 6 % 2 = 0  -> es par
valores_pares = [v for v in valores if v % 2 == 0]

# Imprimimos solo los números pares
print(valores_pares)


# ==========================================
# EJERCICIO 3
# Convertir grados Fahrenheit a Celsius
# ==========================================

# Lista de temperaturas en grados Fahrenheit
temperatura_fahrenheit = [32, 212, 275]

# Fórmula matemática:
# Celsius = (Fahrenheit - 32) * 5/9
#
# Primero se resta 32
# Luego se multiplica por 5/9
#
# Ejemplo:
# 32°F  -> (32 - 32) * 5/9 = 0°C
# 212°F -> (212 - 32) * 5/9 = 100°C
grados_celsius = [(f - 32) * (5 / 9) for f in temperatura_fahrenheit]

# Imprimimos las temperaturas convertidas a Celsius
print(grados_celsius)