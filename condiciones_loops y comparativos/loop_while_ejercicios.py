# ==========================================
# EJERCICIO 1
# Imprimir números en pantalla del 10 al 0
# ==========================================

# Creamos una variable que empieza en 10
numeros = 10

# Mientras numeros sea mayor o igual a 0, el ciclo se seguirá ejecutando
while numeros >= 0:

    # Imprimimos el valor actual de numeros
    print(numeros)

    # Restamos 1 en cada vuelta para evitar un ciclo infinito
    numeros = numeros - 1


# ==========================================
# EJERCICIO 2
# Restar números desde 50 hasta 0
# Mostrar solo los números divisibles entre 5
# ==========================================

# Creamos una variable que empieza en 50
numero = 50

# Mientras numero sea mayor o igual a 0, el ciclo continúa
while numero >= 0:

    # Verificamos si el número es divisible entre 5
    # El operador % obtiene el residuo de una división
    # Si numero % 5 es igual a 0, significa que sí es divisible entre 5
    if numero % 5 == 0:
        print(numero)

    # Restamos 1 en cada vuelta del ciclo
    # Esto permite revisar todos los números desde 50 hasta 0
    numero = numero - 1


# ==========================================
# EJERCICIO 3
# Recorrer una lista con for
# Imprimir cada número hasta encontrar un número negativo
# ==========================================

# Lista con números positivos, negativos y cero
lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, -3, 4, -7, 0, 2, 6, -1]

# Recorremos cada elemento de la lista
for numero in lista_numeros:

    # Si el número es negativo, se interrumpe el ciclo por completo
    if numero < 0:
        break

    # Si el número no es negativo, se imprime en pantalla
    print(numero)