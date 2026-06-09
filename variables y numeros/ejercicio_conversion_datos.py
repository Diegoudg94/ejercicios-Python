num1 = 4.6  # Guardamos un número decimal tipo float
num_entero = int(num1)  # Convertimos el número decimal a entero
print(num_entero)  # Imprime el número convertido: 4
print(type(num_entero))  # Imprime el tipo de dato: int

#ejercicio2 
num2 = 10  # Guardamos un número entero tipo int
num2_float = float(num2)  # Convertimos el número entero a decimal tipo float
print(type(num2_float))  # Imprime el tipo de dato resultante: float

#ejercicio3
num1 = "9.4"  # Guardamos un número decimal, pero está escrito como texto/string
num2 = "10"  # Guardamos un número entero, pero también está como texto/string
# Convertimos ambos textos a números decimales con float() y los sumamos
print(float(num1) + float(num2))