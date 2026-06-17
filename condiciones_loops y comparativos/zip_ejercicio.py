# ==========================================
# EJERCICIO 1
# Unir capitales con sus países usando zip()
# ==========================================

# Lista de capitales
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]

# Lista de países en el mismo orden que sus capitales
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# zip() une los elementos que están en la misma posición
# Ejemplo: "Berlín" con "Alemania"
combinados = zip(capitales, paises)

# Recorremos las parejas creadas por zip()
# Primero recibimos la capital y luego el país
for capital, pais in combinados:

    # Imprimimos una frase usando cada capital y su país
    print(f"{capital} es la capital de {pais}")


# ==========================================
# EJERCICIO 2
# Unir marcas con productos usando zip()
# ==========================================

# Lista de marcas
marcas = ["Nike", "Apple", "Jose Cuervo"]

# Lista de productos en el mismo orden que sus marcas
productos = ["tenis", "iPhone", "tequila"]

# zip() une cada marca con su producto
combinados = zip(marcas, productos)

# Convertimos el resultado de zip en una lista para poder verlo
print(list(combinados))


# ==========================================
# EJERCICIO 3
# Unir números en español, portugués e inglés
# ==========================================

# Listas con los números del 1 al 5 en tres idiomas
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

# zip() une los elementos que están en la misma posición
# Ejemplo: "uno", "um", "one"
numeros = list(zip(espanol, portugues, ingles))

# Imprimimos la lista de tuplas creada
print(numeros)