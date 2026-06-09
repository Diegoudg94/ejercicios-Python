# Función format()
# Sirve para insertar valores dentro de un texto.
# La sintaxis es:
# print("Mi auto es {} y su matrícula es {}".format(color_auto, matricula))

color_auto = "rojo"
matricula = "ABC123"

print("Mi auto es {} y su matrícula es {}".format(color_auto, matricula))

# version mas limpia # Cadenas literales o f-strings
# Se coloca una f antes de las comillas.
# Permiten insertar variables directamente dentro del texto usando llaves {}.
# Imprime un texto usando f-string.
# Las variables color_auto y matricula se insertan directamente dentro del texto.
print(f"Mi auto es {color_auto} y su matrícula es {matricula}")


# Guardamos dos números en variables
x = 10
i = 5

# Sumamos los dos números y guardamos el resultado en z
z = x + i

# Imprime los valores de x e i usando f-string
print(f"Mis números son {x} y {i}")

# Imprime los valores de x, i y también el resultado de la suma
print(f"Mis números son {x} y {i} y la suma es {z}")


# Forma más sencilla usando cadenas literales o f-strings

# Guardamos el color del auto
color = "rojo"

# Guardamos la matrícula del auto
matricula = 123456

# Imprime el color y la matrícula usando f-string
print(f"Mi auto es {color} y su matrícula es {matricula}")
