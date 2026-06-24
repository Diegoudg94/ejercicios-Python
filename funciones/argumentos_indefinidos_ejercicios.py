# --------------------------------------------------
# EJERCICIO 1: SUMA DE CUADRADOS
# --------------------------------------------------

# Creamos una función lambda llamada suma_cuadrados
# *args permite recibir una cantidad indefinida de números
# Por ejemplo: suma_cuadrados(2, 4, 5)
suma_cuadrados = lambda *args: sum([x**2 for x in args])

# x**2 significa elevar cada número al cuadrado
# La comprensión de lista [x**2 for x in args] crea una lista con los cuadrados
# sum() suma todos esos cuadrados
print(suma_cuadrados(2, 4, 5, 6, 11, 90, 760))


# --------------------------------------------------
# EJERCICIO 2: SUMA DE VALORES ABSOLUTOS
# --------------------------------------------------

# Creamos una función lambda llamada suma_absolutos
# *args permite recibir varios números
suma_absolutos = lambda *args: sum([abs(x) for x in args])

# abs(x) convierte cada número a su valor absoluto
# Es decir, si un número es negativo, lo vuelve positivo
# Ejemplo: abs(-5) da 5
print(suma_absolutos(2, 4, 6, 2, 122, 4))


# --------------------------------------------------
# EJERCICIO 3: NOMBRE + SUMA DE NÚMEROS
# --------------------------------------------------

# Definimos una función llamada numeros_persona
# nombre recibe el primer dato
# *args recibe todos los números que le pasemos después del nombre
def numeros_persona(nombre, *args):
    
    # sum(args) suma todos los números recibidos en *args
    suma = sum(args)
    
    # Retornamos un mensaje usando f-string
    # Dentro de las llaves {} se colocan variables
    return f"Hola {nombre}, la suma de tus números es {suma}"


# Pedimos al usuario su nombre
nombre = input("¿Cuál es tu nombre? ")

# Pedimos 4 números al usuario
# input() recibe texto, por eso usamos int() para convertirlo a número entero
num1 = int(input("Di el primer número: "))
num2 = int(input("Di el segundo número: "))
num3 = int(input("Di el tercer número: "))
num4 = int(input("Di el cuarto número: "))

# Llamamos la función
# Primero mandamos el nombre
# Luego mandamos los 4 números
print(numeros_persona(nombre, num1, num2, num3, num4))