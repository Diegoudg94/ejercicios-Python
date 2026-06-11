# TUPLAS EN PYTHON
# Las tuplas son parecidas a las listas, pero son inmutables.
# Inmutable significa que no puedes cambiar, agregar o eliminar elementos directamente.
# Se escriben normalmente entre paréntesis ().
# También pueden escribirse sin paréntesis, pero es más claro usarlos.

# Las tuplas suelen usarse cuando queremos guardar datos que no deberían cambiar.
# También ocupan menos memoria que una lista.


# Creamos una tupla con dos textos y otra tupla dentro
mi_tupla = ("a", "b", (10, 20))

# type() nos muestra el tipo de dato
print(type(mi_tupla))  # <class 'tuple'>


# Accedemos al primer elemento de la tupla
# Python cuenta desde 0, entonces:
# índice 0 = "a"
# índice 1 = "b"
# índice 2 = (10, 20)
print(mi_tupla[0])  # a


# Imprimimos la tupla completa
print(mi_tupla)


# Accedemos al elemento en el índice 2
# Este elemento es otra tupla: (10, 20)
print(mi_tupla[2])


# Accedemos a un elemento dentro de la tupla anidada
# mi_tupla[2] entra a (10, 20)
# [0] toma el primer valor de esa tupla, que es 10
print(mi_tupla[2][0])  # 10


# Convertimos la tupla en lista usando list()
# Esto permite modificar sus elementos si fuera necesario
mi_tupla = list(mi_tupla)

print(type(mi_tupla))  # <class 'list'>


# Convertimos la lista otra vez en tupla usando tuple()
mi_tupla = tuple(mi_tupla)

print(type(mi_tupla))  # <class 'tuple'>


# Creamos otra tupla con números
t = (1, 2, 3, 2)


# Desempaquetado de tuplas
# Cada valor de la tupla se guarda en una variable
# x = 1
# y = 2
# z = 3
# w = 2
x, y, z, w = t


# Imprimimos todas las variables
print(x, y, z, w)


# Imprimimos solo la variable z
print(z)  # 3


# len() cuenta cuántos elementos tiene la tupla
print(len(t))  # 4


# count() cuenta cuántas veces aparece un valor
# En este caso, el número 2 aparece dos veces
print(t.count(2))  # 2


# index() busca la primera posición donde aparece un valor
# El número 3 está en el índice 2
print(t.index(3))  # 2