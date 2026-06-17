# Elige el palito
# El usuario debe elegir uno de los 4 palitos.
# Si elige el palito más corto, pierde.
# Si elige otro palito, se salva.

from random import shuffle


# ==========================================
# 1. Crear lista inicial
# ==========================================

# Cada string representa un palito de diferente tamaño
palitos = ["-", "--", "---", "----"]


# ==========================================
# 2. Mezclar los palitos
# ==========================================

def mezclar(lista):
    # shuffle() mezcla la lista original
    shuffle(lista)

    # Devolvemos la lista ya mezclada
    return lista


# ==========================================
# 3. Pedir al usuario que elija un palito
# ==========================================

def probar_suerte():
    # Creamos una variable vacía para guardar el intento
    intento = ""

    # Mientras el usuario no escriba 1, 2, 3 o 4,
    # se le seguirá pidiendo una opción válida
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número del 1 al 4: ")

    # Convertimos el intento a número entero
    intento = int(intento)

    # Devolvemos el número elegido
    return intento


# ==========================================
# 4. Comprobar el intento
# ==========================================

def chequear_intento(lista, intento):
    # Restamos 1 porque las listas empiezan en índice 0
    # Si el usuario elige 1, realmente es la posición 0
    seleccion = intento - 1

    # Mostramos qué palito le tocó al usuario
    print(f"Te ha tocado {lista[seleccion]}")

    # Si el palito elegido es el más corto, pierde
    if lista[seleccion] == "-":
        print("A lavar platos")
    else:
        print("Te salvaste")


# ==========================================
# 5. Ejecutar el juego
# ==========================================

# Mezclamos los palitos
palitos_mezclados = mezclar(palitos)

# Pedimos al usuario que elija un número
numero_elegido = probar_suerte()

# Revisamos si ganó o perdió
chequear_intento(palitos_mezclados, numero_elegido)