# *args significa "argumentos variables"
# Sirve para que una función pueda recibir muchos valores,
# aunque no sepamos exactamente cuántos serán.

# Función normal con dos argumentos obligatorios
def suma(num1, num2):
    # Retorna la suma de los dos números recibidos
    return num1 + num2

# Llamamos la función con dos valores
print(suma(5, 3))


# --------------------------------------------------
# ¿Cómo hacemos para sumar más de dos valores?
# Usamos *args
# --------------------------------------------------

def suma(*args):
    # args guarda todos los valores recibidos en forma de tupla
    # Por ejemplo: suma(1,2,3) -> args = (1, 2, 3)

    total = 0  # Aquí iremos acumulando la suma

    # Recorremos cada número dentro de args
    for numero in args:
        # Sumamos cada número al total
        total += numero

    # Devolvemos el resultado final
    return total

# Podemos mandar muchos valores
print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# --------------------------------------------------
# Forma más corta usando sum()
# --------------------------------------------------

def suma(*args):
    # sum(args) suma automáticamente todos los valores recibidos
    return sum(args)

print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#SUMA CUADRADOS 

suma_cuadrados = lambda *args: sum([x**2 for x in args])

print(suma_cuadrados(2,4,5,6,11,90,760))  # 

#ejercicio 2 
suma_absolutos = lambda *args: sum([abs(x) for x in args])  
print(suma_absolutos(2,4,6,2,122,4))

#ejercicio 3


def numeros_persona(nombre, *args):
    suma = sum(args)
    return f"Hola {nombre}, la suma de tus números es {suma}"


nombre = input("¿Cuál es tu nombre? ")

num1 = int(input("Di el primer número: "))
num2 = int(input("Di el segundo número: "))
num3 = int(input("Di el tercer número: "))
num4 = int(input("Di el cuarto número: "))

print(numeros_persona(nombre, num1, num2, num3, num4))