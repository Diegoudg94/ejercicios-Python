# ==========================================
# RANGO / RANGE
# ==========================================

# Modo anterior: usando una lista creada manualmente
lista = [1, 2, 3, 4]

for n in lista:
    print(n)


# Modo nuevo: usando range()
# range(5) genera números desde 0 hasta 4
# El número final no se incluye
for n in range(5):
    print(n)


# range(inicio, final, paso)
# Empieza en 10, llega hasta antes de 20 y avanza de 2 en 2
for n in range(10, 20, 2):
    print(n)


# Empieza en 10, llega hasta antes de 20 y avanza de 3 en 3
for n in range(10, 20, 3):
    print(n)


# Creamos una lista con números del 0 al 100
# Se usa 101 porque el último número no se incluye
mi_lista = list(range(101))

# Mostramos el tipo de dato
print(type(mi_lista))

# Mostramos la lista completa
print(mi_lista)