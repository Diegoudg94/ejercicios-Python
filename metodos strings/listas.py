# LISTAS EN PYTHON
# Las listas se escriben entre corchetes []
# Pueden guardar varios elementos y también se pueden modificar

mi_lista = ["a", "b", "c"]

# type() muestra el tipo de dato
print(type(mi_lista))  # <class 'list'>


# Una lista puede guardar textos, números u otros datos
# Ojo: aquí "2" y "4.4" están entre comillas, por eso son texto
mi_lista = ["Hola", "2", "4.4"]
print(type(mi_lista))


# len() cuenta cuántos elementos tiene la lista
mi_lista = ["a", "b", "c"]
print(len(mi_lista))  # 3

# Accedemos al elemento en el índice 2
# Python cuenta desde 0: a=0, b=1, c=2
print(mi_lista[2])  # c


# Podemos unir listas con +
mi_lista = [1, 2, 3]
mi_otra_lista = [4, 5, 6]

print(mi_lista + mi_otra_lista)

# Guardamos la unión de ambas listas en una nueva variable
mi_gran_lista = mi_lista + mi_otra_lista
print(mi_gran_lista)


# Las listas sí se pueden modificar
# Cambiamos el primer elemento, índice 0
mi_gran_lista[0] = "Uno"
print(mi_gran_lista)


# append() agrega un elemento al final de la lista
mi_gran_lista.append(7)
print(mi_gran_lista)


# pop() elimina el último elemento de la lista
mi_gran_lista.pop()
print(mi_gran_lista)


# pop(0) elimina el elemento en el índice 0
mi_gran_lista.pop(0)
print(mi_gran_lista)


# También podemos guardar el elemento eliminado en una variable
elemento_eliminado = mi_gran_lista.pop(2)

print(mi_gran_lista)
print(elemento_eliminado)


# sort() ordena la lista alfabéticamente
nueva_lista = ["G", "o", "B", "M", "C"]
nueva_lista.sort()
print(nueva_lista)


# sort() también ordena números de menor a mayor
nueva_lista = [1, 0, 4, 8, 20, 10]
nueva_lista.sort()
print(nueva_lista)


# reverse() invierte el orden actual de la lista
nueva_lista = ["G", "o", "B", "M", "C"]
nueva_lista.reverse()
print(nueva_lista)