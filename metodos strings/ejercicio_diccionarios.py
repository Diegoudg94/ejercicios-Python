# --------------------------------------------------
# EJERCICIO 1
# Crear un diccionario llamado mi_dic
# con información de una persona
# --------------------------------------------------

# Un diccionario guarda datos en pares:
# "clave": valor
mi_dic = {
    "nombre": "Karen",
    "Apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# Mostramos el diccionario completo
print(mi_dic)


# --------------------------------------------------
# EJERCICIO 2
# Acceder a un valor dentro de un diccionario anidado
# --------------------------------------------------

# Este diccionario tiene otros diccionarios dentro.
# También tiene una lista dentro de la clave "points2".
mi_dict = {
    "valores_1": {
        "v1": 3,
        "v2": 6
    },
    "puntos": {
        "points1": 9,
        "points2": [10, 300, 15]
    }
}

# Paso por paso:
# mi_dict["puntos"] entra al diccionario "puntos"
# ["points2"] entra a la lista [10, 300, 15]
# [1] toma el elemento en índice 1, que es 300
print(mi_dict["puntos"]["points2"][1])


# --------------------------------------------------
# EJERCICIO 3
# Modificar y agregar datos en un diccionario
# --------------------------------------------------

mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# Cambiamos el valor de la clave "edad"
mi_dic["edad"] = 36

# Cambiamos el valor de la clave "ocupacion"
mi_dic["ocupacion"] = "Editora"

# Agregamos una nueva clave llamada "pais"
# con el valor "Colombia"
mi_dic["pais"] = "Colombia"

# Mostramos el diccionario actualizado
print(mi_dic)