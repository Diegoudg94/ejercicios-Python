# ==========================================
# APUNTES: FUNCIONES dinamicas
# ==========================================

# En estos ejercicios combinamos funciones con:
# - return
# - condiciones
# - range()
# - listas
# - ciclos for


# ==========================================
# EJEMPLO 1
# Revisar si un número tiene 3 cifras
# ==========================================

def chequear_3_cifras(numero):
    # range(100, 1000) incluye números del 100 al 999
    # Si numero está dentro de ese rango, devuelve True
    # Si no está, devuelve False
    return numero in range(100, 1000)


# Probamos con 45
# 45 no tiene 3 cifras, entonces devuelve False
resultado = chequear_3_cifras(45)

# Mostramos el tipo de dato del resultado
# Será bool porque devuelve True o False
print(type(resultado))

# Mostramos el resultado
print(resultado)


# ==========================================
# EJEMPLO 2
# Probar la misma función con un número válido
# ==========================================

def chequear_3_cifras(numero):
    # Revisamos si el número está entre 100 y 999
    return numero in range(100, 1000)


# 435 sí tiene 3 cifras, entonces devuelve True
resultado = chequear_3_cifras(435)

print(type(resultado))
print(resultado)


# ==========================================
# EJEMPLO 3
# Sumar dos números y revisar si el resultado tiene 3 cifras
# ==========================================

def chequear_3_cifras(n1, n2):
    # Sumamos los dos números recibidos
    suma = n1 + n2

    # Revisamos si la suma está entre 100 y 999
    return suma in range(100, 1000)


# 2 + 400 = 402
# 402 tiene 3 cifras, entonces devuelve True
resultado = chequear_3_cifras(2, 400)

print(resultado)


# ==========================================
# EJEMPLO 4
# Revisar si una lista contiene al menos un número de 3 cifras
# ==========================================

mi_lista = [55, 99, 100]

def chequear_3_cifras(lista):
    # Recorremos cada número dentro de la lista
    for l in lista:

        # Si encontramos un número entre 100 y 999,
        # la función devuelve True y termina
        if l in range(100, 1000):
            return True

    # Si termina el for y no encontró ningún número de 3 cifras,
    # devuelve False
    return False


# La lista tiene el número 100, entonces devuelve True
resultado = chequear_3_cifras(mi_lista)

print(resultado)


# ==========================================
# EJEMPLO 5
# Lista sin números de 3 cifras
# ==========================================

mi_lista = [55, 99, 1600]

def chequear_3_cifras(lista):
    # Recorremos cada número de la lista
    for l in lista:

        # Revisamos si el número tiene 3 cifras
        if l in range(100, 1000):
            return True

    # Si ningún número cumple la condición, devuelve False
    return False


# 55 no tiene 3 cifras
# 99 no tiene 3 cifras
# 1600 tiene 4 cifras
# Entonces devuelve False
resultado = chequear_3_cifras(mi_lista)

print(resultado)


# ==========================================
# EJEMPLO 6
# Crear una lista solo con los números de 3 cifras
# ==========================================

mi_lista = [555, 99, 800]

def chequear_3_cifras(lista):
    # Creamos una lista vacía para guardar los números de 3 cifras
    lista_3_cifras = []

    # Recorremos cada número de la lista original
    for l in lista:

        # Si el número está entre 100 y 999,
        # lo agregamos a la nueva lista
        if l in range(100, 1000):
            lista_3_cifras.append(l)

    # Devolvemos la lista con los números de 3 cifras encontrados
    return lista_3_cifras


# En esta lista, 555 y 800 tienen 3 cifras
resultado = chequear_3_cifras(mi_lista)

print(resultado)