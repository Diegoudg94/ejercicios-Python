# ==========================================
# EJERCICIO 1: COMPARAR DOS NÚMEROS
# ==========================================

# Pedimos al usuario que ingrese el primer número.
# input() siempre recibe texto, por eso usamos int()
# para convertir ese texto en número entero.
num1 = int(input("Ingresa un número: "))

# Pedimos al usuario que ingrese el segundo número.
num2 = int(input("Ingresa otro número: "))

# Si num1 es mayor que num2, se ejecuta este bloque.
if num1 > num2:
    print(f"{num1} es mayor que {num2}")

# Si num1 no es mayor, pero es igual a num2,
# se ejecuta este bloque.
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")

# Si ninguna de las condiciones anteriores se cumple,
# significa que num2 es mayor que num1.
else:
    print(f"{num2} es mayor que {num1}")


# ==========================================
# EJERCICIO 2: VALIDAR SI UNA PERSONA PUEDE CONDUCIR
# ==========================================

# Guardamos la edad de la persona.
edad = 16

# Guardamos si la persona tiene licencia.
# False significa que NO tiene licencia.
# True significaría que SÍ tiene licencia.
tiene_licencia = False

# Para poder conducir, la persona necesita:
# 1. Tener 18 años o más
# 2. Tener licencia
#
# Esta condición usa OR porque basta con que una de estas cosas sea cierta
# para que NO pueda conducir:
# - que sea menor de edad
# - que no tenga licencia
if edad < 18 or not tiene_licencia:
    print("No puedes conducir")

# Si no se cumple la condición anterior,
# significa que la persona tiene 18 o más
# y además sí tiene licencia.
else:
    print("Puedes conducir")


# ==========================================
# EJERCICIO 3: VALIDAR REQUISITOS PARA POSTULARSE
# ==========================================

# Pedimos al usuario que indique si habla inglés.
# strip() elimina espacios al inicio o al final.
# lower() convierte la respuesta a minúsculas.
ingles = input("¿Hablas inglés? ").strip().lower()

# Pedimos al usuario que indique si sabe Python.
python = input("¿Sabes Python? ").strip().lower()

# Convertimos la respuesta del usuario a un valor booleano.
# Si escribió "si" o "sí", entonces sabes_ingles será True.
# Si escribió cualquier otra cosa, será False.
if ingles == "si" or ingles == "sí":
    sabes_ingles = True
else:
    sabes_ingles = False

# Hacemos lo mismo con la respuesta sobre Python.
if python == "si" or python == "sí":
    sabes_python = True
else:
    sabes_python = False

# Caso 1:
# Si sabe inglés Y también sabe Python,
# cumple con todos los requisitos.
if sabes_ingles and sabes_python:
    print("Cumples con los requisitos")

# Caso 2:
# Si sabe inglés, pero NO sabe Python,
# entonces solo le falta Python.
elif sabes_ingles and not sabes_python:
    print("Para postularte necesitas saber Python")

# Caso 3:
# Si sabe Python, pero NO sabe inglés,
# entonces solo le falta inglés.
elif sabes_python and not sabes_ingles:
    print("Para postularte necesitas saber inglés")

# Caso 4:
# Si no entró en ninguno de los casos anteriores,
# significa que no sabe inglés ni Python.
else:
    print("Para postularte necesitas saber inglés y Python")