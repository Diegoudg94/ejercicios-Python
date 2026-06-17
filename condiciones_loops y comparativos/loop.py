# ==========================================
# LOOPS / BUCLES EN PYTHON
# ==========================================

# Un loop o bucle sirve para hacer que un bloque de código
# se ejecute más de una vez.
#
# En lugar de escribir muchas veces la misma instrucción,
# usamos un loop para repetirla automáticamente.


# ==========================================
# EJEMPLO 1: REPETIR CÓDIGO SIN LOOP Y CON LOOP
# ==========================================

# Ejemplo sin loop:
# Aquí repetimos manualmente la misma instrucción 3 veces.
print("Hola")
print("Hola")
print("Hola")


# Ejemplo con loop:
# range(3) genera una secuencia de 3 vueltas: 0, 1, 2.
# La variable i toma un valor distinto en cada vuelta.
for i in range(3):
    print("Hola")


# ==========================================
# EJEMPLO 2: RECORRER UNA LISTA
# ==========================================

# Creamos una lista con tres letras.
mi_lista = ["a", "b", "c"]

# Recorremos la lista elemento por elemento.
# En cada vuelta, la variable letra toma un valor de la lista.
for letra in mi_lista:

    # index() nos dice en qué posición está el elemento dentro de la lista.
    # Ojo: los índices en Python empiezan en 0.
    numero_letra = mi_lista.index(letra)

    # Imprimimos la letra.
    print(letra)

    # Imprimimos un mensaje concatenando texto con la variable letra.
    print("La letra es: " + letra)

    # Imprimimos un mensaje usando f-string.
    # Los f-strings permiten meter variables dentro de un texto.
    print(f"La letra {letra} está en el índice {numero_letra}")


# ==========================================
# EJEMPLO 3: FILTRAR ELEMENTOS CON IF DENTRO DE UN LOOP
# ==========================================

# Creamos una lista de nombres.
lista = ["Pablo", "Luis", "Federico", "Laura", "Julia"]

# Recorremos cada nombre dentro de la lista.
for nombre in lista:

    # startswith("L") revisa si el texto empieza con la letra L.
    if nombre.startswith("L"):
        print(nombre)

    # Si el nombre no empieza con L, se ejecuta el else.
    else:
        print(f"{nombre} no empieza con L")


# ==========================================
# EJEMPLO 4: SUMAR NÚMEROS CON UN LOOP
# ==========================================

# Creamos una lista de números.
numeros = [1, 2, 3, 4, 5]

# Creamos una variable acumuladora.
# Empieza en 0 porque todavía no hemos sumado nada.
valor = 0

# Recorremos cada número de la lista.
for numero in numeros:

    # En cada vuelta, sumamos el número actual al valor acumulado.
    valor = valor + numero

    # Imprimimos el valor en cada paso para ver cómo va creciendo.
    print(valor)

# Al terminar el loop, imprimimos el resultado final.
print(valor)


# ==========================================
# EJEMPLO 5: RECORRER UN STRING
# ==========================================

# Un string también es iterable.
# Eso significa que se puede recorrer letra por letra.
palabra = "Python"

for letra in palabra:
    print(letra)


# ==========================================
# EJEMPLO 6: RECORRER UNA LISTA DE NÚMEROS
# ==========================================

# Aquí la variable se llama palabra, pero realmente guarda una lista.
# Sería más claro llamarla numeros.
palabra = [1, 2, 3, 4, 5]

# Recorremos cada elemento de la lista.
for letra in palabra:
    print(letra)


# ==========================================
# EJEMPLO 7: RECORRER UNA LISTA DE LISTAS
# ==========================================

# Esta es una lista que contiene otras listas dentro.
for objeto in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:

    # En cada vuelta, objeto representa una lista completa.
    print(objeto)


# ==========================================
# EJEMPLO 8: DESEMPAQUETAR LISTAS DENTRO DE UN LOOP
# ==========================================

# Cada lista interna tiene exactamente 3 elementos.
# Por eso podemos guardarlos en 3 variables: a, b y c.
for a, b, c in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:

    # En la primera vuelta:
    # a = 1, b = 2, c = 3
    #
    # En la segunda vuelta:
    # a = 4, b = 5, c = 6
    #
    # En la tercera vuelta:
    # a = 7, b = 8, c = 9

    print(a)
    print(b)
    print(c)


# ==========================================
# EJEMPLO 9: RECORRER UN DICCIONARIO CON .items()
# ==========================================

# Creamos un diccionario.
# Un diccionario guarda información en pares clave: valor.
dic = {
    "clave1": "a",
    "clave2": "b",
    "clave3": "c"
}

# .items() permite recorrer la clave y el valor al mismo tiempo.
for clave, valor in dic.items():

    # Imprimimos la clave.
    print(clave)

    # Imprimimos el valor asociado a esa clave.
    print(valor)


# ==========================================
# EJEMPLO 10: MISMO EJEMPLO, PERO CON OTROS NOMBRES DE VARIABLES
# ==========================================

dic = {
    "clave1": "a",
    "clave2": "b",
    "clave3": "c"
}

# Aquí usamos a y b en lugar de clave y valor.
# Funciona igual, pero es menos descriptivo.
#
# a representa la clave.
# b representa el valor.
for a, b in dic.items():
    print(a)
    print(b)