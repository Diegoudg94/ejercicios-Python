# ==========================================
# MATCH / CASE EN PYTHON
# ==========================================

# match / case sirve para comparar un valor contra varios casos posibles.
# Es parecido a usar varios if / elif / else.
# IMPORTANTE: match solo funciona en Python 3.10 o superior.


# ==========================================
# EJEMPLO 1: COMPARAR UNA SERIE
# ==========================================

# Guardamos una serie en una variable.
serie = "N-02"

# Este bloque está comentado con triple comilla.
# Es la versión usando if / elif / else.
'''
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe esa serie")
'''

# Ahora hacemos la misma comparación, pero usando match / case.
match serie:

    # Si serie vale "N-01", imprime Samsung.
    case "N-01":
        print("Samsung")

    # Si serie vale "N-02", imprime Nokia.
    case "N-02":
        print("Nokia")

    # Si serie vale "N-03", imprime Motorola.
    case "N-03":
        print("Motorola")

    # El guion bajo _ funciona como caso por defecto.
    # Es parecido al else.
    # Si no coincide con ningún caso anterior, entra aquí.
    case _:
        print("No existe esa serie")


# ==========================================
# EJEMPLO 2: MATCH CON DICCIONARIOS
# ==========================================

# Creamos un diccionario llamado cliente.
# Un diccionario guarda información usando pares clave: valor.
cliente = {
    "nombre": "Federico",
    "edad": 50,
    "ocupacion": "instructor"
}

# Creamos un diccionario llamado pelicula.
# Este diccionario tiene otro diccionario dentro,
# llamado "ficha_tecnica".
pelicula = {
    "titulo": "Matrix",
    "ficha_tecnica": {
        "protagonista": "Keanu Reeves",
        "director": "Lana y Lily Wachowski"
    }
}

# Creamos un diccionario llamado libro.
libro = {
    "titulo": "1984",
    "autor": "George Orwell"
}

# Guardamos los tres diccionarios dentro de una lista.
# Así podemos recorrerlos uno por uno.
elementos = [cliente, pelicula, libro]

# Recorremos cada elemento de la lista.
# En cada vuelta, la variable e toma el valor de un diccionario.
for e in elementos:

    # Usamos match para revisar qué estructura tiene cada diccionario.
    match e:

        # Caso 1:
        # Si el diccionario tiene las claves:
        # "nombre", "edad" y "ocupacion",
        # entonces asumimos que es un cliente.
        #
        # Además, guardamos los valores en variables:
        # nombre, edad y ocupacion.
        case {
            "nombre": nombre,
            "edad": edad,
            "ocupacion": ocupacion
        }:
            print("Este es un cliente")
            print(nombre, edad, ocupacion)

        # Caso 2:
        # Si el diccionario tiene una clave "titulo"
        # y una clave "ficha_tecnica",
        # entonces asumimos que es una película.
        #
        # Dentro de "ficha_tecnica" buscamos:
        # "protagonista" y "director".
        case {
            "titulo": titulo,
            "ficha_tecnica": {
                "protagonista": protagonista,
                "director": director
            }
        }:
            print("Esta es una película")
            print(titulo, protagonista, director)

        # Caso 3:
        # Si el diccionario tiene las claves:
        # "titulo" y "autor",
        # entonces asumimos que es un libro.
        case {
            "titulo": titulo,
            "autor": autor
        }:
            print("Este es un libro")
            print(titulo, autor)

        # Caso por defecto:
        # Si el elemento no coincide con ninguno de los patrones anteriores,
        # entra aquí.
        case _:
            print("No sé qué es esto")