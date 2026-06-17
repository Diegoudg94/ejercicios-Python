# ==========================================
# EJERCICIO 1
# Crear una lista con números del 2500 al 2586
# ==========================================

# range(2500, 2587) empieza en 2500 y termina en 2586
# Se pone 2587 porque el último número no se incluye
mi_lista = list(range(2500, 2587))

# Imprimimos la lista completa
print(mi_lista)


# ==========================================
# EJERCICIO 2
# Crear una lista con múltiplos de 3 del 3 al 3000
# ==========================================

# range(3, 3001, 3) significa:
# empezar en 3, llegar hasta 3000 y avanzar de 3 en 3
mi_lista = list(range(3, 3001, 3))

# Imprimimos la lista completa
print(mi_lista)


# ==========================================
# EJERCICIO 3
# Sumar los cuadrados de los números del 1 al 15
# ==========================================

# Variable donde guardaremos la suma total
suma_cuadrados = 0

# Recorremos los números del 1 al 15
# Se pone 16 porque range no incluye el último número
for numero in range(1, 16):

    # Calculamos el cuadrado del número actual
    cuadrado = numero ** 2

    # Sumamos el cuadrado al total
    suma_cuadrados += cuadrado

# Imprimimos el resultado final
print("La suma es:", suma_cuadrados)