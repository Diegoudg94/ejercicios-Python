# ==========================================
# EJERCICIO 1
# Objetivo: revisar si todos los números de una lista son positivos
# ==========================================

mi_lista = [1, 4, 6]

def todos_positivos(lista):
    # Recorremos la lista número por número
    for numero in lista:

        # Si aparece un número negativo, ya no todos son positivos
        if numero < 0:
            return False

    # Si no encontró negativos, todos son positivos
    return True


resultado = todos_positivos(mi_lista)
print(resultado)


# ==========================================
# EJERCICIO 2
# Objetivo: sumar solo los números mayores a 0 y menores a 1000
# ==========================================

mi_lista = [1, 4, 6]

def suma_menores(lista):
    # Variable donde se acumula la suma
    suma = 0

    # Revisamos cada número de la lista
    for numero in lista:

        # Solo sumamos si está entre 1 y 999
        if numero > 0 and numero < 1000:
            suma += numero

    # Devolvemos la suma total
    return suma


resultado = suma_menores(mi_lista)
print(resultado)


# ==========================================
# EJERCICIO 3
# Objetivo: obtener los números pares de una lista
# ==========================================

lista_numeros = [1, 4, 6, 5, 10]

def cantidad_pares(lista):
    # Lista donde guardaremos los números pares
    pares = []

    # Revisamos cada número
    for numero in lista:

        # Si el residuo al dividir entre 2 es 0, es par
        if numero % 2 == 0:
            pares.append(numero)

    # Devolvemos la lista de pares encontrados
    return pares


resultado = cantidad_pares(lista_numeros)
print(resultado)