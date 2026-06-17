# ==========================================
# APUNTES: RETURN EN FUNCIONES
# ==========================================

# return sirve para devolver un resultado desde una función.
# Ese resultado se puede guardar en una variable.

# OJO:
# Cuando Python encuentra un return, la función termina ahí.


# ==========================================
# EJEMPLO 1
# Función para sumar
# ==========================================

def sumar(num1, num2):
    # Esta función recibe dos números y devuelve su suma
    return num1 + num2


# Guardamos el resultado de la función en una variable
resultado1 = sumar(5, 3)

# Imprimimos el resultado
print(resultado1)


# ==========================================
# EJEMPLO 2
# Función para multiplicar
# ==========================================

def multiplicar(num1, num2):
    # Esta función recibe dos números y devuelve su multiplicación
    return num1 * num2


# Guardamos el resultado de multiplicar 2 por 3
resultado2 = multiplicar(2, 3)

# Imprimimos el resultado
print(resultado2)


# ==========================================
# EJEMPLO 3
# Función para dividir
# ==========================================

def dividir(num1, num2):
    # Esta función recibe dos números y devuelve su división
    return num1 / num2


# Guardamos el resultado de dividir 10 entre 2
resultado3 = dividir(10, 2)

# Imprimimos el resultado
print(resultado3)


# ==========================================
# SUMAR LOS RESULTADOS
# ==========================================

# Como los return se guardaron en variables,
# podemos usar esas variables para hacer otra operación
print(resultado1 + resultado2 + resultado3)