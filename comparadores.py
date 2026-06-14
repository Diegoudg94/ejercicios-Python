# ==========================================
# OPERADORES LÓGICOS EN PYTHON
# ==========================================

# Los operadores lógicos permiten combinar
# expresiones booleanas (True o False).

# and = ambas condiciones deben ser True
# or  = al menos una condición debe ser True
# not = invierte el resultado lógico

# ==========================================
# OPERADOR AND
# ==========================================

# Ambas condiciones son verdaderas:
# 4 es menor que 5 -> True
# 5 es igual a 2 + 3 -> True
# True and True = True

mi_bool = (4 < 5) and (5 == 2 + 3)
print(mi_bool)  # True


# ==========================================
# OPERADOR OR
# ==========================================

# Basta con que una condición sea verdadera
# para que el resultado sea True.

# Ambas condiciones son verdaderas
# True or True = True

mi_bool = (10 == 10) or (3 == 3)
print(mi_bool)  # True


# Ninguna condición es verdadera
# False or False = False

mi_bool = (10 == 9) or (3 == 2)
print(mi_bool)  # False


# ==========================================
# OPERADORES LÓGICOS CON TEXTO
# ==========================================

texto = "esta frase es breve"

# Verificamos que las palabras "frase"
# y "breve" existan dentro del texto.
# True and True = True

mi_bool = ("frase" in texto) and ("breve" in texto)
print(mi_bool)  # True


texto = "esta frase es breve"

# Verificamos si existe "hola" o "breve".
# "hola" no existe -> False
# "breve" sí existe -> True
# False or True = True

mi_bool = ("hola" in texto) or ("breve" in texto)
print(mi_bool)  # True


# ==========================================
# OPERADOR NOT
# ==========================================

# NOT invierte el resultado lógico.

# "a" == "a" da True
# not True = False

mi_bool = not ("a" == "a")
print(mi_bool)  # False


# "a" != "a" da False
# not False = True

mi_bool = not ("a" != "a")
print(mi_bool)  # True
