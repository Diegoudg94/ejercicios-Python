#Ejercicio 1
def saludar(): # Esta funcion dice hola mundo 
    print("Hola mundo")

saludar()
# Ejercicio 2
def bienvenida(nombre_persona): # Esta funcion devuelve un saludo de la persona 
    print(f"Bienvenido {nombre_persona}")

bienvenida("Juan")

#Ejercicio 3
from random import *
def cuadrado (): ## esta funcion calcula el cuadrado de un numero aleatorio 
    numero = randint(1,200)
    resultado = numero ** 2
    print(f"El numero es {numero}")
    print(f"El cuadrado es {resultado}")

cuadrado()
