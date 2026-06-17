# ==========================================
# EJERCICIO 1: SALUDAR A CADA ALUMNO DE UNA LISTA
# ==========================================

# Creamos una lista con los nombres de los alumnos.
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

# Recorremos la lista alumno por alumno.
# En cada vuelta, la variable nombre toma un valor diferente de la lista.
for nombre in alumnos_clase:

    # Imprimimos un saludo personalizado usando f-string.
    print(f"Hola {nombre}")


# ==========================================
# EJERCICIO 2: SUMAR TODOS LOS NÚMEROS DE UNA LISTA
# ==========================================

# Creamos una lista con varios números.
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Creamos una variable acumuladora.
# Empieza en 0 porque todavía no hemos sumado ningún número.
suma_numeros = 0

# Recorremos cada número dentro de la lista.
for numero in lista_numeros:

    # Sumamos el número actual al acumulador.
    # Esto es lo mismo que escribir:
    # suma_numeros = suma_numeros + numero
    suma_numeros += numero

# Imprimimos el resultado final de la suma.
print("La suma de los números es:", suma_numeros)


# ==========================================
# EJERCICIO 3: SUMAR PARES E IMPARES POR SEPARADO
# ==========================================

# Creamos una lista con varios números.
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Creamos una variable para acumular la suma de números pares.
suma_pares = 0

# Creamos una variable para acumular la suma de números impares.
suma_impares = 0

# Recorremos cada número dentro de la lista.
for numero in lista_numeros:

    # El operador % obtiene el residuo de una división.
    # Si numero % 2 es igual a 0, significa que el número es par.
    if numero % 2 == 0:

        # Si el número es par, lo sumamos a suma_pares.
        suma_pares += numero

    # Si el número no es par, entonces es impar.
    else:

        # Si el número es impar, lo sumamos a suma_impares.
        suma_impares += numero

# Imprimimos la suma total de los números pares.
print("La suma de los números pares es:", suma_pares)

# Imprimimos la suma total de los números impares.
print("La suma de los números impares es:", suma_impares)