# ==========================================
# EJERCICIO 1
# Crear una función que calcule una potencia
# ==========================================

def potencia(num1, num2):
    # Esta función recibe dos números:
    # num1 será la base
    # num2 será el exponente
    # Ejemplo: 3 ** 4 significa 3 elevado a la cuarta potencia
    return num1 ** num2


# Llamamos la función y guardamos el resultado en una variable
resultado = potencia(3, 4)

# Imprimimos el resultado
print(resultado)


# ==========================================
# EJERCICIO 2
# Convertir dólares a euros
# ==========================================

def usd_a_eur(usd):
    # Esta función recibe una cantidad en dólares
    # y la convierte a euros usando una tasa de 0.90
    # Ejemplo: 100 dólares * 0.90 = 90 euros
    return usd * 0.90


# Llamamos la función con 100 dólares
# El resultado realmente está en euros
euros = usd_a_eur(100)

# Imprimimos la cantidad convertida
print(euros)


# ==========================================
# EJERCICIO 3
# Invertir una palabra y convertirla a mayúsculas
# ==========================================

def invertir_palabra(palabra):
    # Convertimos la palabra a mayúsculas
    palabra = palabra.upper()

    # Invertimos la palabra usando slicing
    # [::-1] recorre el texto desde el final hasta el inicio
    palabra_invertida = palabra[::-1]

    # Devolvemos la palabra invertida
    return palabra_invertida


# Llamamos la función con la palabra "Python"
resultado = invertir_palabra("Python")

# Imprimimos el resultado
print(resultado)