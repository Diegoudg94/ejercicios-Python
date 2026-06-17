# Importamos todas las funciones del módulo random
# Lo usamos para generar un número aleatorio
from random import *

# Pedimos el nombre del usuario
nombre = input("Ingresa tu nombre: ")

# Saludamos al usuario usando su nombre
print(f"Hola {nombre}")

# randint(8, 100) genera un número aleatorio entre 8 y 100
# Este será el número que el usuario debe adivinar
numero_sistema = randint(8, 100)

# Esta línea solo sirve para pruebas
# En el juego real deberías quitarla, porque muestra la respuesta
print(numero_sistema)

# El usuario tendrá 8 intentos para adivinar
intentos = 8

# El ciclo se repetirá mientras todavía queden intentos
while intentos > 0:

    # Pedimos al usuario que escriba un número
    # int() convierte el texto ingresado en número entero
    numero_usuario = int(input("Pensé un número del 8 al 100. Adivina: "))

    # Verificamos si el número está fuera del rango permitido
    # Si es menor que 8 o mayor que 100, no es válido
    if numero_usuario < 8 or numero_usuario > 100:
        print("No permitido")

    # Si el número del usuario es menor que el número secreto,
    # le avisamos que el número correcto es más grande
    elif numero_usuario < numero_sistema:
        print("Incorrecto, el número es mayor")

    # Si el número del usuario es mayor que el número secreto,
    # le avisamos que el número correcto es más pequeño
    elif numero_usuario > numero_sistema:
        print("Incorrecto, el número es menor")

    # Si no se cumple ninguna condición anterior,
    # significa que el usuario acertó
    else:
        print(f"Felicitaciones {nombre}, ganaste")

        # break corta el ciclo porque el usuario ya ganó
        break

    # Restamos 1 intento después de cada vuelta del ciclo
    intentos = intentos - 1

    # Mostramos cuántos intentos quedan
    print(f"Te quedan {intentos} intentos")

# Este else pertenece al while
# Se ejecuta solo si el ciclo termina porque se acabaron los intentos
# No se ejecuta si el ciclo termina con break
else:
    print("No tienes más intentos")