# Ejercicio 1
# Extrae la primera palabra de la frase usando slicing.

frase = "Controlar la complejidad es la esencia de la programación"

# frase[0:9] significa:
# empieza en el índice 0 y termina antes del índice 9.
# Esto extrae la palabra "Controlar".
extraccion = frase[0:9]

print(extraccion)  # Controlar


# Ejercicio 2
# Toma cada tercer carácter empezando desde el noveno carácter
# hasta el final de la frase.

frase1 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

# En Python se cuenta desde 0.
# Entonces el noveno carácter está en el índice 8.
#
# frase1[8::3] significa:
# empieza en el índice 8,
# llega hasta el final,
# y toma caracteres de 3 en 3.
extraccion1 = frase1[8::3]

print(extraccion1)


# Ejercicio 3
# Invierte la frase completa usando slicing.

frase2 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

# frase2[::-1] significa:
# recorre toda la frase, pero de derecha a izquierda.
extraccion2 = frase2[::-1]

print(extraccion2)


# Extra
# Invertir una frase que parece palíndromo.

palindromo = "Anita lava la tina"

# Esto invierte el texto completo.
# Ojo: aquí solo lo estamos volteando, no estamos comprobando si es palíndromo.
extraccion3 = palindromo[::-1]

print(extraccion3)