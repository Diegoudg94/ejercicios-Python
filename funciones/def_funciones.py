# ==========================================
# APUNTES: FUNCIONES EN PYTHON
# ==========================================

# Una función es un bloque de código que podemos reutilizar.
# Sirve para no repetir el mismo código muchas veces.

# Para crear una función usamos la palabra def.

# Estructura básica:
# def nombre_de_la_funcion():
#     código que se ejecuta cuando llamamos la función


# ==========================================
# EJEMPLO 1
# Función sin parámetros
# ==========================================

def saludar_persona():
    """
    Esta función muestra un saludo en pantalla.
    """
    print("Hola, bienvenido a la función")


# Para que una función se ejecute, debemos llamarla o invocarla.
# Si no la llamamos, Python solo la guarda, pero no la ejecuta.
saludar_persona()


# ==========================================
# EJEMPLO 2
# Función con parámetro
# ==========================================

# Pedimos el nombre al usuario
nombre = input("Ingrese su nombre: ")

def saludar_persona(nombre):
    """
    Esta función recibe un nombre y muestra un saludo personalizado.
    """
    print(f"Hola {nombre}, bienvenido a la función")


# Llamamos la función y le pasamos la variable nombre
saludar_persona(nombre)


# ==========================================
# EJEMPLO 3
# Pasar un valor directamente a la función
# ==========================================

def saludar_persona(nombre):
    """
    Esta función recibe un nombre y lo usa dentro del saludo.
    """
    print(f"Hola {nombre}, bienvenido a la función")


# Aquí pasamos el nombre directamente
saludar_persona("Juan")