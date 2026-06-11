# ============================
# BOOLEANOS EN PYTHON
# ============================

# Un booleano es un tipo de dato que solo puede tener dos valores:
# True  -> Verdadero
# False -> Falso

mi_bool_1 = True
mi_bool_2 = False

# type() muestra el tipo de dato de una variable
print(type(mi_bool_1))  # <class 'bool'>


# ============================
# BOOLEANOS CON COMPARACIONES
# ============================

# Las comparaciones devuelven un resultado booleano:
# True si la comparación es verdadera
# False si la comparación es falsa

mi_bool_1 = 5 < 4
print(mi_bool_1)  # False, porque 5 no es menor que 4

mi_bool_2 = 5 > 4
print(mi_bool_2)  # True, porque 5 sí es mayor que 4


# ============================
# OPERADORES DE COMPARACIÓN
# ============================

# Diccionario de símbolos:
# >   mayor que
# <   menor que
# >=  mayor o igual que
# <=  menor o igual que
# ==  igual que
# !=  diferente que

# Al usar estos operadores, siempre obtendremos
# un resultado booleano: True o False.


# ============================
# CREAR BOOLEANOS DIRECTAMENTE
# ============================

var1 = True
var2 = False

print(type(var1))  # <class 'bool'>
print(type(var2))  # <class 'bool'>


# ============================
# CREAR BOOLEANOS MEDIANTE EXPRESIONES
# ============================

# Esta comparación devuelve False porque 5 no es mayor que 5
numero = 5 > 5

print(type(numero))  # <class 'bool'>
print(numero)        # False


# Esta comparación devuelve True porque 5 es igual a 5
numero = 5 == 5

print(type(numero))  # <class 'bool'>
print(numero)        # True


# Esta comparación devuelve True porque 5 es menor o igual que 5
numero = 5 <= 5

print(numero)  # True


# Esta comparación devuelve False porque 5 no es diferente de 5
numero = 5 != 5

print(numero)  # False


# ============================
# USAR bool()
# ============================

# bool() convierte una expresión en un valor booleano
numero = bool(5 != 3)

print(numero)  # True, porque 5 sí es diferente de 3


# Si usamos bool() vacío, devuelve False automáticamente
numero = bool()

print(numero)  # False


# ============================
# BOOLEANOS CON LISTAS
# ============================

# Creamos una lista con números
lista = [1, 2, 3, 4, 5]

# in revisa si un elemento está dentro de una lista
control = 5 in lista

print(control)  # True, porque 5 sí está en la lista


# ============================
# USAR in Y not
# ============================

lista = [1, 2, 3, 4, 5]

# Revisamos si el número 7 está en la lista
control = 7 in lista

print(control)      # False, porque 7 no está en la lista

# not invierte el valor booleano
# Si control es False, not control será True
print(not control)  # True

# Mostramos el tipo de dato
print(type(control))  # <class 'bool'>