# Guardamos tres números en variables
x = 6
y = 2
z = 7


# Suma: x + y
print(f"{x} más {y} es igual a {x + y}")

# Resta: x - y
print(f"{x} menos {y} es igual a {x - y}")

# Multiplicación: x * y
print(f"{x} por {y} es igual a {x * y}")

# División normal: x / y
# El resultado normalmente sale como decimal tipo float
print(f"{x} entre {y} es igual a {x / y}")


# División al piso: z // y
# Divide y devuelve solo la parte entera del resultado
print(f"{z} dividido al piso por {y} es igual a {z // y}")


# Módulo: z % y
# Devuelve el residuo o sobrante de una división
print(f"{z} módulo por {y} es igual a {z % y}")

# El módulo sirve para identificar números pares e impares:
# Si numero % 2 da 0, el número es par
# Si numero % 2 da 1, el número es impar


# Potencia: x ** y
# Eleva x a la potencia indicada por y
print(f"{x} elevado a la {y} es igual a {x ** y}")

# También podemos elevar un número al cubo usando exponente 3
print(f"{x} elevado al cubo es igual a {x ** 3}")


# Raíz cuadrada
# Elevar a 0.5 es lo mismo que sacar raíz cuadrada
print(f"La raíz cuadrada de {x} es {x ** 0.5}")

# Raíz cúbica
# Elevar a 1/3 es lo mismo que sacar raíz cúbica
print(f"La raíz cúbica de {x} es {x ** (1/3)}")