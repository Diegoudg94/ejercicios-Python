'''
LOOP WHILE

Un ciclo while se ejecuta mientras una condición sea verdadera.

Estructura básica:

while condicion:
    # código que se repite mientras la condición sea True
else:
    # código que se ejecuta cuando la condición deja de ser True

IMPORTANTE:
Hay que tener cuidado con los ciclos infinitos.
Un ciclo infinito ocurre cuando la condición nunca cambia a False.

Palabras importantes:

break    -> corta/interrumpe el ciclo por completo
continue -> salta una vuelta del ciclo y pasa a la siguiente
pass     -> no hace nada, solo sirve como marcador temporal
'''

# ==========================================
# EJEMPLO 1: WHILE CON CONTADOR
# ==========================================

monedas = 5

# Mientras monedas sea mayor que 0, el ciclo se seguirá ejecutando
while monedas > 0:
    print(f"Tengo {monedas} monedas")

    # Restamos 1 moneda en cada vuelta del ciclo
    # Esto evita que el ciclo sea infinito
    monedas = monedas - 1

# El else se ejecuta cuando la condición del while ya no se cumple
else:
    print("No tengo más dinero")


# ==========================================
# EJEMPLO 2: WHILE CON INPUT DEL USUARIO
# ==========================================

respuesta = "s"

# Mientras la respuesta sea "s", el programa sigue preguntando
while respuesta == "s":
    respuesta = input("¿Quieres seguir? s/n: ")

# Cuando la respuesta ya no sea "s", termina el ciclo
else:
    print("Fin")


# ==========================================
# EJEMPLO 3: USO DE PASS
# ==========================================

respuesta = "s"

# OJO:
# Este ciclo se vuelve infinito porque respuesta nunca cambia.
# pass no hace nada, solo deja pasar el código.
# Por eso este ejemplo NO se debe ejecutar así.

while respuesta == "s":
    pass

print("Fin")


# ==========================================
# EJEMPLO 4: USO DE BREAK
# ==========================================

nombre = input("Ingresa tu nombre: ")

# Recorremos cada letra del nombre
for letra in nombre:

    # Si la letra es "r", el ciclo se rompe completamente
    if letra == "r":
        break

    # Se imprimen las letras hasta antes de encontrar la "r"
    print(letra)


# ==========================================
# EJEMPLO 5: USO DE CONTINUE
# ==========================================

nombre = input("Ingresa tu nombre: ")

# Recorremos cada letra del nombre
for letra in nombre:

    # Si la letra es "r", se salta esa vuelta del ciclo
    # Es decir, no imprime la "r", pero continúa con las demás letras
    if letra == "r":
        continue

    print(letra)