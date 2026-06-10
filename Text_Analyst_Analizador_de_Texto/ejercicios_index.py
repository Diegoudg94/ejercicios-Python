# Ejercicio 1:
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición
# dentro de la siguiente palabra: "ordenador"

palabra = "ordenador"
print(palabra[4])


# Ejercicio 2:
# Encuentra y muestra en pantalla el índice de la primera aparición
# de la palabra "práctica"

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
indice_practica = frase.index("práctica")
print(indice_practica)


# Ejercicio 3:
# Encuentra y muestra en pantalla el índice de la última aparición
# de la palabra "práctica"

indice_ultima_practica = frase.rindex("práctica")
print(indice_ultima_practica)