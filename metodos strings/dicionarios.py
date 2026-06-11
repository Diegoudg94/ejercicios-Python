# DICCIONARIOS EN PYTHON
# Un diccionario es una colección de datos que funciona con pares:
# clave : valor

# Se escriben entre llaves {}

# La clave es como el nombre o etiqueta del dato.
# El valor es la información que está guardada en esa clave.

# Los diccionarios se usan cuando queremos guardar información
# y encontrarla por su nombre, no por su posición.

# A diferencia de las listas, donde accedemos a los elementos por índice,
# en los diccionarios accedemos usando una clave.

# Ejemplo de idea:
# En una lista importa la posición del dato.
# En un diccionario importa el nombre de la clave.

# Se recomienda usar diccionarios cuando queremos representar datos
# con una relación clara, por ejemplo:
# nombre, edad, país, correo, teléfono, etc.

# -------------------------------
# DICCIONARIOS EN PYTHON
# -------------------------------

# Un diccionario vacío se crea con llaves {}
diccionario = {}

# Un diccionario guarda información en pares:
# "clave": "valor"
diccionario = {
    "Clave1": "valor1",
    "Clave2": "valor2"
}

# Las claves deben ser únicas.
# No puede haber dos claves iguales en el mismo diccionario.

# type() nos dice qué tipo de dato es
print(type(diccionario))  # <class 'dict'>


# Para obtener un valor, usamos su clave entre corchetes []
resultado = diccionario["Clave1"]
print(resultado)  # valor1


# Ejemplo de diccionario con información de un cliente
cliente = {
    "Nombre": "Juan",
    "Apellido": "Fuentes",
    "Peso": 70,
    "Talla": 1.76
}

# Imprime todo el diccionario
print(cliente)

# Imprime solo el valor guardado en la clave "Apellido"
print(cliente["Apellido"])  # Fuentes


# -------------------------------
# DICCIONARIOS CON LISTAS Y OTROS DICCIONARIOS
# -------------------------------

dic = {
    "c1": 55,
    "c2": [10, 20, 30],
    "c3": {"a": 100, "b": 200, "c": 300}
}

# Accedemos a la lista que está en "c2"
# Luego tomamos el elemento en índice 1
# Recuerda: Python cuenta desde 0
print(dic["c2"][1])  # 20

# Accedemos al diccionario que está dentro de "c3"
# Luego tomamos el valor de la clave "b"
print(dic["c3"]["b"])  # 200


# -------------------------------
# ACCEDER A ELEMENTOS DENTRO DE LISTAS
# -------------------------------

dic = {
    "clave 1": ["a", "b", "c"],
    "clave 2": ["d", "e", "f"]
}

# Primero entramos a "clave 2"
# Eso nos da la lista ["d", "e", "f"]
# Luego tomamos el índice 1, que es "e"
print(dic["clave 2"][1])  # e


# Podemos aplicar métodos al resultado
# upper() convierte el texto a mayúsculas
print(dic["clave 2"][1].upper())  # E


# -------------------------------
# AGREGAR ELEMENTOS A UN DICCIONARIO
# -------------------------------

dic = {
    "1": "a",
    "2": "b"
}

print(dic)

# Agregamos una nueva clave "3" con el valor "c"
dic["3"] = "c"

print(dic)

# También podemos usar números como claves
# Ojo: 2 no es lo mismo que "2"
# 2 es número entero
# "2" es texto
dic[2] = "e"

print(dic)


# -------------------------------
# MÉTODOS IMPORTANTES
# -------------------------------

# keys() muestra todas las claves del diccionario
print(dic.keys())

# values() muestra todos los valores del diccionario
print(dic.values())

# items() muestra los pares clave-valor
print(dic.items())