#ejercicio 1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] 
valor_minimo = min(lista_numeros)
print(valor_minimo)
valor_maximo = max(lista_numeros)
print(valor_maximo)
## ejercicio 2
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(rango)

#ejercicio 3
# ==========================================
# EJERCICIO 1
# Encontrar el valor mínimo y máximo de una lista
# ==========================================

# Lista con operaciones matemáticas
# Python primero resuelve las operaciones y luego guarda los resultados en la lista
lista_numeros = [
    44542247 / 2,
    21310 / 5,
    2134747 * 33,
    44556475,
    121676,
    6654067,
    353254,
    123134,
    55 ** 12,
    611 ** 5
]

# min() obtiene el valor más pequeño de la lista
valor_minimo = min(lista_numeros)
print(valor_minimo)

# max() obtiene el valor más grande de la lista
valor_maximo = max(lista_numeros)
print(valor_maximo)


# ==========================================
# EJERCICIO 2
# Calcular el rango de una lista de números
# ==========================================

# Lista de números
lista_numeros = [
    44542247,
    21310,
    2134747,
    44556475,
    121676,
    6654067,
    353254,
    123134,
    552512,
    611665
]

# El rango se obtiene restando:
# valor máximo - valor mínimo
rango = max(lista_numeros) - min(lista_numeros)

# Imprimimos el resultado del rango
print(rango)


# ==========================================
# EJERCICIO 3
# Obtener datos de un diccionario
# ==========================================

# Diccionario con nombres como claves y edades como valores
diccionario_edades = {
    "Carlos": 55,
    "María": 42,
    "Mabel": 78,
    "José": 44,
    "Lucas": 24,
    "Rocío": 35,
    "Sebastián": 19,
    "Catalina": 2,
    "Darío": 49
}

# .values() obtiene solo las edades del diccionario
# min() obtiene la edad más pequeña
edad_minima = min(diccionario_edades.values())
print(edad_minima)

# max() aplicado directamente al diccionario revisa las claves
# En este caso, busca el nombre más alto en orden alfabético
ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)