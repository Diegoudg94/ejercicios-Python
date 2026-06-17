# ==========================================
# APUNTES: ZIP EN PYTHON
# ==========================================

# zip() sirve para unir dos o más listas elemento por elemento.
# Une los elementos que están en la misma posición.

# Ejemplo:
# lista1 = ["Berlín", "Tokio"]
# lista2 = ["Alemania", "Japón"]
#
# zip(lista1, lista2) uniría:
# "Berlín" con "Alemania"
# "Tokio" con "Japón"


# ==========================================
# EJERCICIO 1
# Unir capitales con sus países usando zip()
# ==========================================

# Lista de capitales
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]

# Lista de países
# Deben estar en el mismo orden que sus capitales
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# zip() une los elementos que están en la misma posición
# Ejemplo:
# "Berlín" se une con "Alemania"
# "Tokio" se une con "Japón"
combinados = zip(capitales, paises)

# Recorremos las parejas creadas por zip()
# Como usamos zip(capitales, paises):
# primero recibimos la capital
# después recibimos el país
for capital, pais in combinados:

    # Imprimimos una frase con cada capital y su país
    print(f"{capital} es la capital de {pais}")


# ==========================================
# EJERCICIO 2
# Unir marcas con productos usando zip()
# ==========================================

# Lista de marcas
marcas = ["Nike", "Apple", "Jose Cuervo"]

# Lista de productos
# Cada producto corresponde a la marca en la misma posición
productos = ["tenis", "iPhone", "tequila"]

# zip() une cada marca con su producto
# Nike con tenis
# Apple con iPhone
# Jose Cuervo con tequila
combinados = zip(marcas, productos)

# zip() crea un objeto zip
# Para ver su contenido completo, lo convertimos en lista con list()
print(list(combinados))


# ==========================================
# EJERCICIO 3
# Unir números en español, portugués e inglés
# ==========================================

# Lista de números en español
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]

# Lista de números en portugués
portugues = ["um", "dois", "três", "quatro", "cinco"]

# Lista de números en inglés
ingles = ["one", "two", "three", "four", "five"]

# zip() también puede unir más de dos listas
# En este caso une:
# español + portugués + inglés
#
# Ejemplo:
# "uno", "um", "one"
# "dos", "dois", "two"
numeros = list(zip(espanol, portugues, ingles))

# Imprimimos la lista de tuplas creada
print(numeros)


# ==========================================
# RESUMEN RÁPIDO
# ==========================================

# zip() une listas por posición.
# list(zip()) convierte el resultado en una lista.
# Cada combinación queda guardada como una tupla.
# El orden de las listas importa.
# Si una lista es más corta, zip() se detiene ahí.