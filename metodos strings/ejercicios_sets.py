# ============================
# EJERCICIO 1
# Unión de sets
# ============================

# Creamos el primer set con números y strings
mi_set_1 = {1, 2, "tres", "cuatro"}

# Creamos el segundo set
mi_set_2 = {"tres", 4, 5}

# union() une los dos sets en uno solo.
# Si hay elementos repetidos, solo se guardan una vez.
mi_set_3 = mi_set_1.union(mi_set_2)

# Imprimimos el nuevo set unido
print(mi_set_3)


# ============================
# EJERCICIO 2
# Eliminar un elemento aleatorio con pop()
# ============================

# Creamos un set con nombres de personas
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# pop() elimina un elemento aleatorio del set.
# Como los sets no tienen orden fijo, no sabemos exactamente cuál eliminará.
sorteo.pop()

# Imprimimos el set después de eliminar un elemento
print(sorteo)


# ============================
# EJERCICIO 3
# Agregar un elemento a un set
# ============================

# Creamos nuevamente el set con nombres de personas
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# add() agrega un nuevo elemento al set
sorteo.add("Damián")

# Imprimimos el set con el nuevo elemento agregado
print(sorteo)