#Ejercicio lanzar dados
from random import *
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print(f"El primer dado es {dado1}")
    print(f"El segundo dado es {dado2}")

lanzar_dados()

from random import randint

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
# ejercicio 2 reducir lista

lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista):

    # Lista donde guardaremos los números sin repetir
    lista_sin_duplicados = []

    for numero in lista:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)

    # Eliminamos el número más grande
    lista_sin_duplicados.remove(max(lista_sin_duplicados))

    return lista_sin_duplicados


def promedio(lista):
    suma = 0

    for numero in lista:
        suma += numero

    return suma / len(lista)


lista_reducida = reducir_lista(lista_numeros)

print(lista_reducida)      # [1, 2, 7]
print(promedio(lista_reducida))  # 3.3333333333333335



### cara o cruz

from random import choice

# Lista de números que vamos a usar en el ejercicio
lista_numeros = [1, 2, 3, 4, 5]

# Esta función no recibe argumentos
# Solo devuelve "Cara" o "Cruz" al azar
def lanzar_moneda():
    return choice(["Cara", "Cruz"])


# Esta función recibe:
# 1. El resultado de la moneda
# 2. Una lista de números
def probar_suerte(moneda, lista):

    # Si la moneda salió Cara
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []

    # Si no salió Cara, entonces salió Cruz
    else:
        print("La lista fue salvada")
        return lista


# Guardamos el resultado del lanzamiento
resultado = lanzar_moneda()

# Probamos la suerte usando el resultado y la lista
print(probar_suerte(resultado, lista_numeros))


## cara o cruz 2

# Importamos choice para elegir un elemento al azar
from random import choice

# Creamos una lista con las dos opciones posibles
caras = ["cara", "cruz"]

# Esta función recibe una lista y devuelve una opción al azar
def lanzar_moneda(lista):
    return choice(lista)


# Esta función recibe el resultado de la moneda
def probar_suerte(moneda):

    # Pedimos al usuario que escriba cara o cruz
    intento = input("Ingrese cara o cruz: ")

    # Comparamos lo que escribió el usuario con el resultado real
    if intento == moneda:
        return "Ganaste"
    else:
        return "Perdiste"


# Guardamos el resultado aleatorio de lanzar la moneda
resultado_moneda = lanzar_moneda(caras)

# Evaluamos si el usuario acertó o no
print(probar_suerte(resultado_moneda))

# Mostramos cuál fue el resultado real
print(f"La moneda cayó en: {resultado_moneda}")