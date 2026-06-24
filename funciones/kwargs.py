# --------------------------------------------------
# **kwargs significa "keyword arguments"
# Sirve para recibir una cantidad indefinida de argumentos con nombre
# Por ejemplo: x=3, y=4, z=5
# Python los guarda como un diccionario
# --------------------------------------------------

def suma(**kwargs):
    # Mostramos qué tipo de dato es kwargs
    # El resultado será <class 'dict'> porque kwargs es un diccionario
    print(type(kwargs))


# Llamamos la función mandando argumentos con nombre
suma(x=3, y=4, z=5)


# --------------------------------------------------
# SUMAR LOS VALORES DE **kwargs
# --------------------------------------------------

def suma(**kwargs):
    # Creamos una variable para acumular la suma
    total = 0

    # kwargs.items() nos permite recorrer el diccionario
    # clave será el nombre del argumento: x, y, z
    # valor será el número asignado: 3, 4, 5
    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")

        # Sumamos cada valor al total
        total += valor

    # El return debe ir fuera del for
    # Así espera a terminar de sumar todos los valores
    return total


# Aquí se imprime el resultado final de la suma
print(suma(x=3, y=4, z=5))


# --------------------------------------------------
# COMBINANDO ARGUMENTOS NORMALES, *args Y **kwargs
# --------------------------------------------------

def prueba(num1, num2, *args, **kwargs):
    # El orden correcto es:
    # 1. argumentos normales
    # 2. *args
    # 3. **kwargs

    # num1 y num2 son argumentos obligatorios
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    # *args guarda los argumentos extra sin nombre
    # En este caso: 3, 4, 123, 3
    for arg in args:
        print(f"arg es igual a {arg}")

    # **kwargs guarda los argumentos extra con nombre
    # En este caso: x=3, y=4, z=5
    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")


# Llamamos la función:
# 5 y 11 van a num1 y num2
# 3, 4, 123, 3 van a *args
# x=3, y=4, z=5 van a **kwargs
prueba(5, 11, 3, 4, 123, 3, x=3, y=4, z=5)


# --------------------------------------------------
# DESEMPACAR LISTAS Y DICCIONARIOS
# --------------------------------------------------

# Esta lista se puede mandar como *args
lista_args = [3, 4, 5, 6, 2, 1, 3]

# Este diccionario se puede mandar como **kwargs
dic_kwargs = {"x": 3, "y": 4, "z": 5}

# El * antes de lista_args desempaca la lista
# Es como escribir:
# prueba(5, 11, 3, 4, 5, 6, 2, 1, 3, ...)
#
# El ** antes de dic_kwargs desempaca el diccionario
# Es como escribir:
# x=3, y=4, z=5
prueba(5, 11, *lista_args, **dic_kwargs)