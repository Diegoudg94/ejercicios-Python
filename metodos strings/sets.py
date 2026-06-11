# ============================
# SETS EN PYTHON
# ============================

# Un set es una colección de elementos, parecido a una lista,
# pero con características especiales:
# - No permite elementos repetidos.
# - No mantiene un orden fijo.
# - No se accede por índices como en las listas.
# - Solo puede contener elementos inmutables, como números, strings o tuplas.
# - Se puede declarar con set() o directamente con llaves {}.


# Crear un set usando set()
mi_set = set([1, 2, 3, 4])

# type() muestra el tipo de dato
print(type(mi_set))

# Imprime el contenido del set
print(mi_set)


# Crear un set usando llaves {}
otro_set = {1, 2, 3, 4}

print(type(otro_set))
print(otro_set)


# Los sets eliminan automáticamente los elementos repetidos
otro_set = {1, 1, 1, 3, 4, 4, 5}

# Aunque escribimos números repetidos, Python solo guarda uno de cada valor
print(otro_set)


# Un set puede contener distintos tipos de datos inmutables:
# números, strings y tuplas.
# No puede contener listas, porque las listas son mutables.
otro_set = set([1, 2, 3, "Hola", (2, 3, 4)])

print(otro_set)


# Crear otro set
s = set([1, 2, 3, 4, 5])

# len() devuelve la cantidad de elementos del set
print(len(s))

print(s)


# ============================
# VERIFICAR SI UN ELEMENTO EXISTE
# ============================

# Devuelve True si el elemento está en el set
print(1 in s)

# Devuelve False si el elemento no está en el set
print(6 in s)

# Devuelve True si el elemento NO está en el set
print(6 not in s)


# ============================
# UNIÓN DE SETS
# ============================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# union() une dos sets y elimina elementos repetidos
s3 = s1.union(s2)

print(s3)


# ============================
# AGREGAR ELEMENTOS A UN SET
# ============================

# add() agrega un elemento al set
s1.add(2)

# Como el 2 ya existía, el set no cambia
print(s1)

# Agregamos el número 4
s1.add(4)

print(s1)

# Si volvemos a agregar 4, no se repite
s1.add(4)

print(s1)


# ============================
# ELIMINAR ELEMENTOS DE UN SET
# ============================

# remove() elimina un elemento específico.
# Si el elemento no existe, produce un error.
s1.remove(2)

print(s1)


# discard() también elimina un elemento,
# pero si el elemento no existe, NO produce error.
s1.discard(3)

print(s1)


# pop() elimina un elemento aleatorio del set.
# Como los sets no tienen orden fijo, no sabemos exactamente cuál eliminará.
s1.pop()

print(s1)


# También podemos guardar en una variable el elemento eliminado por pop()
sorteo = s1.pop()

print(sorteo)


# ============================
# VACIAR UN SET
# ============================

# clear() elimina todos los elementos del set
s1.clear()

print(s1)