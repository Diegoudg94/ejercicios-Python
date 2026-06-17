# ==========================================
# EJERCICIOS CON ENUMERATE
# ==========================================

# enumerate() sirve para recorrer una lista, cadena u otro iterable
# y obtener al mismo tiempo:
# - el índice, es decir, la posición
# - el valor, es decir, el elemento


# ==========================================
# EJERCICIO 1
# Mostrar cada nombre junto con su índice
# ==========================================

# Lista con nombres
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Recorremos la lista usando enumerate()
# indice guarda la posición del nombre
# nombre guarda el valor de cada elemento
for indice, nombre in enumerate(lista_nombres):

    # Imprimimos cada nombre con su posición
    print(f"{nombre} se encuentra en el índice {indice}")


# ==========================================
# EJERCICIO 2
# Crear una lista con el índice y cada letra de una cadena
# ==========================================

# Cadena de texto
cadena = "Python"

# Creamos una lista de tuplas usando list comprehension
# Cada tupla contiene: índice y caracter
lista_indices = [(indice, caracter) for indice, caracter in enumerate(cadena)]

# Imprimimos la lista creada
print(lista_indices)


# ==========================================
# EJERCICIO 3
# Mostrar solo los nombres que empiezan con la letra "M"
# junto con su índice
# ==========================================

# Lista con nombres
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Recorremos la lista obteniendo índice y nombre
for indice, nombre in enumerate(lista_nombres):

    # startswith("M") revisa si el nombre empieza con la letra M
    if nombre.startswith("M"):

        # Imprimimos solo los nombres que cumplen la condición
        print(f"{nombre} se encuentra en el índice {indice}")