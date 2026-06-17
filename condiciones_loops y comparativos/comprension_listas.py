# ==========================================
# APUNTES: COMPRENSIÓN DE LISTAS
# ==========================================

# La comprensión de listas sirve para crear listas de forma más corta.
# Es una forma resumida de escribir un ciclo for que llena una lista.

# Estructura básica:
# nueva_lista = [elemento for elemento in iterable]


# ==========================================
# FORMA LARGA
# ==========================================

# Creamos una palabra
palabra = "python"

# Creamos una lista vacía
lista = []

# Recorremos cada letra de la palabra
for letra in palabra:

    # Agregamos cada letra a la lista
    lista.append(letra)

# Imprimimos la lista final
print(lista)


# ==========================================
# FORMA CORTA
# ==========================================

# Hacemos lo mismo, pero usando comprensión de listas
palabra = "python"

# Por cada letra en palabra, agrega esa letra a la lista
lista = [letra for letra in palabra]

print(lista)


# ==========================================
# EJEMPLO CON STRING DIRECTO
# ==========================================

# También podemos recorrer directamente un texto
lista = [letra for letra in "Palabra"]

print(lista)


# ==========================================
# EJEMPLO CON RANGE
# ==========================================

# Creamos una lista con números pares del 0 al 20
# range(0, 21, 2) empieza en 0, llega hasta 20 y avanza de 2 en 2
lista = [n for n in range(0, 21, 2)]

print(lista)


# ==========================================
# MODIFICAR EL VALOR ANTES DE GUARDARLO
# ==========================================

# Creamos una lista con números pares del 0 al 20
# pero cada número se multiplica por 2 antes de guardarse
lista = [n * 2 for n in range(0, 21, 2)]

print(lista)


# ==========================================
# COMPRENSIÓN DE LISTAS CON IF
# ==========================================

# Guardamos solo los números que cumplen una condición
# En este caso, solo se guardan los números cuyo doble sea mayor que 10
lista = [n for n in range(0, 21, 2) if n * 2 > 10]

print(lista)


# ==========================================
# COMPRENSIÓN DE LISTAS CON IF / ELSE
# ==========================================

# Si n * 2 es mayor que 10, guarda n
# Si no, guarda el texto "no"
lista = [n if n * 2 > 10 else "no" for n in range(0, 21, 2)]

print(lista)


# ==========================================
# EJEMPLO: CONVERTIR PIES A METROS
# ==========================================

# Lista con medidas en pies
pies = [10, 20, 30, 40, 50]

# Convertimos cada valor de pies a metros
# 1 metro equivale aproximadamente a 3.281 pies
metros = [p / 3.281 for p in pies]

print(metros)


