from random import choice

# definir variables principales del juego
# palabras: contiene las posibles palabras secretas
# abecedario: sirve para validar que el usuario escriba letras reales
palabras = ["mexico", "canada", "alemania", "italia", "japon", "china"]
abecedario = "abcdefghijklmnopqrstuvwxyz"


# funcion para elegir palabra oculta
# ¿por qué usamos una función?
# porque así separamos la lógica de elegir una palabra
# y podemos reutilizarla fácilmente
def elegir_palabra(lista_palabras):
    return choice(lista_palabras)


# funcion para mostrar el tablero
# ¿por qué usamos una función?
# porque el tablero se muestra muchas veces durante el juego:
# al inicio, después de cada intento, al ganar o al perder
def mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas):
    tablero = []

    # recorremos cada letra de la palabra secreta
    for letra in palabra:

        # si la letra ya fue adivinada, la mostramos
        if letra in letras_correctas:
            tablero.append(letra)

        # si aún no fue adivinada, mostramos un guion bajo
        else:
            tablero.append("_")

    # mostramos el estado actual del juego
    print("\n" + "*" * 20)
    print(" ".join(tablero))
    print("Letras incorrectas:", " ".join(letras_incorrectas))
    print(f"Tienes {vidas} vidas")
    print("*" * 20 + "\n")


# funcion para pedir letras al usuario
# ¿por qué usamos una función?
# porque pedir y validar una letra requiere varios pasos:
# revisar que sea una letra, que sea solo un caracter
# y que no se haya usado antes
def pedir_letra(letras_utilizadas):
    while True:
        letra = input("Ingresa una letra pista son paises ;): ").lower()

        # si no es una letra del abecedario o escribe más de un caracter
        if letra not in abecedario or len(letra) != 1:
            print("No es una letra válida, elige otra")

        # si la letra ya fue usada antes
        elif letra in letras_utilizadas:
            print("Ya has elegido esa letra, elige otra")

        # si pasa todas las validaciones, regresamos la letra
        else:
            return letra


# funcion para verificar letras
# ¿por qué usamos una función?
# porque aquí decidimos si la letra del usuario es correcta o incorrecta
# y también actualizamos las listas y las vidas
def chequear_letra(letra, palabra, letras_correctas, letras_incorrectas, vidas):

    # si la letra está dentro de la palabra secreta
    if letra in palabra:
        letras_correctas.append(letra)

    # si la letra no está, se guarda como incorrecta y pierde una vida
    else:
        letras_incorrectas.append(letra)
        vidas -= 1

    # regresamos vidas porque su valor pudo cambiar
    return vidas


# funcion para verificar si ha ganado
# ¿por qué usamos una función?
# porque después de cada intento necesitamos revisar
# si el usuario ya descubrió todas las letras de la palabra
def verificar_victoria(palabra, letras_correctas):

    # revisamos letra por letra de la palabra secreta
    for letra in palabra:

        # si alguna letra todavía no está en letras_correctas,
        # significa que aún no ha ganado
        if letra not in letras_correctas:
            return False

    # si terminó el ciclo y no faltó ninguna letra, ganó
    return True


# funcion para iniciar juego
# ¿por qué usamos una función?
# porque aquí organizamos todo el flujo principal:
# elegir palabra, pedir letras, mostrar tablero,
# revisar errores, vidas, victoria o derrota
def jugar():

    # elegir palabra aleatoria
    palabra = elegir_palabra(palabras)

    # listas para guardar el progreso del jugador
    letras_correctas = []
    letras_incorrectas = []

    # definir vidas iniciales
    vidas = 6

    # esta variable controla cuándo termina el while
    juego_terminado = False

    # mientras el juego no haya terminado, se repite el ciclo
    while not juego_terminado:

        # mostrar estado actual del juego
        mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)

        # juntar letras correctas e incorrectas
        # esto sirve para evitar que el usuario repita letras
        letras_usadas = letras_correctas + letras_incorrectas

        # pedir una letra válida al usuario
        letra = pedir_letra(letras_usadas)

        # revisar si la letra está o no en la palabra
        vidas = chequear_letra(
            letra,
            palabra,
            letras_correctas,
            letras_incorrectas,
            vidas
        )

        # si las vidas llegan a cero, el jugador pierde
        if vidas == 0:
            mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
            print("Has perdido. La palabra era:", palabra)
            juego_terminado = True

        # si ya adivinó todas las letras, gana
        elif verificar_victoria(palabra, letras_correctas):
            mostrar_tablero(palabra, letras_correctas, letras_incorrectas, vidas)
            print("Has ganado. La palabra era:", palabra)
            juego_terminado = True


# llamar la función principal para iniciar el programa
jugar()