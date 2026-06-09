 #int num enteros
#float decimales
#metodo round (round) permite eliminar decimales
# round() sirve para redondear números

print(round(3.134))  # Redondea al número entero más cercano: 3

print(round(3.444, 1))  # Redondea dejando 1 decimal: 3.4
# El número después de la coma indica cuántos decimales queremos conservar


print(90 / 7)  # Divide 90 entre 7 y muestra el resultado con decimales

print(round(90 / 7))  # Redondea el resultado de la división al entero más cercano


# Guardamos el resultado redondeado de 90 / 7 en una variable
resultado = round(90 / 7)

print(resultado)  # Muestra el resultado guardado en la variable


# Guardamos un número decimal largo
valor = 95.666666666

print(round(valor, 2))  # Redondea el valor dejando 2 decimales

print(round(valor, 3))  # Redondea el valor dejando 3 decimales

print(type(valor))  # Muestra el tipo de dato de valor: float