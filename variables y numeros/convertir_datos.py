# Casting es el proceso de convertir un tipo de dato en otro.
# En Python existen dos tipos principales de conversión:
# 1. Conversión implícita: Python la hace automáticamente.
# 2. Conversión explícita: el programador la hace manualmente usando funciones como str(), int(), float(), etc.

# Conversión explícita de entero a string
mi_valor = 1              # Se crea una variable con un número entero
otro_valor = str(mi_valor) # Se convierte el número entero a texto usando str()

print(otro_valor)         # Imprime el valor convertido a string


# Conversión implícita
num1 = 20                 # Variable de tipo int
num2 = 30.5               # Variable de tipo float

print(type(num1))         # Muestra el tipo de dato de num1: int
print(type(num2))         # Muestra el tipo de dato de num2: float

# Al sumar un int con un float, Python convierte automáticamente el resultado a float
num1 = num1 + num2

print(type(num1))         # Ahora num1 es de tipo float porque el resultado fue 50.5
print(type(num2))         # num2 sigue siendo float


# Conversión explícita
num1 = 5.8                # Variable de tipo float
print(num1)               # Imprime el valor original: 5.8
print(type(num1))         # Muestra que num1 es de tipo float

# Se convierte el número decimal a entero usando int()
# Ojo: int() no redondea, solo elimina la parte decimal
num2 = int(num1)

print(num2)               # Imprime 5, porque se eliminó el .8
print(type(num2))         # Muestra que num2 ahora es de tipo int

# input() siempre guarda lo que escribe el usuario como texto, es decir, como string
edad = input("escribe tu edad: ")

# Aquí mostramos el tipo de dato de la variable edad
# En este momento será <class 'str'>
print(type(edad))

# Convertimos la edad de texto a número entero usando int()
edad = int(edad)

# Ahora mostramos nuevamente el tipo de dato
# Después de convertirla, será <class 'int'>
print(type(edad))

# Creamos una nueva variable sumándole 1 a la edad
nueva_edad = edad + 1

# Imprimimos la nueva edad
print(nueva_edad)