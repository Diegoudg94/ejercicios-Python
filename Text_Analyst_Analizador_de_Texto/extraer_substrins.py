# Extraer substrings con slicing
# Slicing sirve para obtener partes de un texto.
# Sintaxis general: texto[inicio:fin:salto]
# Nota: el índice "fin" no se incluye.

texto = "ABCDEFGHIJKLM"

# Python cuenta desde 0:
# A  B  C  D  E  F  G  H  I  J  K  L  M
# 0  1  2  3  4  5  6  7  8  9 10 11 12

# Extrae solo el carácter en el índice 2
fragmento = texto[2]
print(fragmento)  # C

# Extrae desde el índice 2 hasta antes del índice 5
fragmento_l = texto[2:5]
print(fragmento_l)  # CDE

# Extrae desde el índice 2 hasta el final
fragmento_final = texto[2:]
print(fragmento_final)  # CDEFGHIJKLM

# Extrae desde el inicio hasta antes del índice 5
inicio_final = texto[:5]
print(inicio_final)  # ABCDE

# Extrae desde el índice 2 hasta antes del 10, saltando de 2 en 2
salto = texto[2:10:2]
print(salto)  # CEGI

# Extrae todo el texto saltando de 3 en 3
salto1 = texto[::3]
print(salto1)  # ADGJM

# Invierte el texto completo
negativo = texto[::-1]
print(negativo)  # MLKJIHGFEDCBA