#  FUNCION ROUND SIRVE PARA REDONDEAR NUMEROS
print(round(3.9)) 
print(round(4.9))
print(round(1.1))
print(round(5.5))
print(round(5.4))


# Redondear a N decimales
print(round(3.14159, 2))  # 3.14
print(round(3.14159, 3))  # 3.142
print(round(3.14159, 4))  # 3.1416

# Ejemplo práctico: precios
precio = 19.99
impuesto = precio * 0.16
print(round(impuesto, 2))  # 3.2

#round() vs int()  round(3.7) da 4 (redondea). int(3.7) da 3 (trunca). Son diferentes: round aproxima al más cercano, int simplemente corta los decimales.

