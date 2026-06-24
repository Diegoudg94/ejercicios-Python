def cantidad_atributos(**kwargs):
    # kwargs guarda los argumentos con nombre en forma de diccionario
    # Ejemplo: x=1, y=2 se convierte en {"x": 1, "y": 2}
    
    # len(kwargs) cuenta cuántos argumentos se recibieron
    return len(kwargs)


print(cantidad_atributos(nombre="Diego", edad=30, ciudad="Guadalajara"))

#ejercicio 2

def lista_atributos(**kwargs):
    # **kwargs recibe argumentos con nombre
    # Ejemplo:
    # nombre="Diego", edad=30
    # se convierte en:
    # {"nombre": "Diego", "edad": 30}

    # kwargs.values() obtiene solo los valores del diccionario
    # En este ejemplo sería: "Diego", 30

    # list() convierte esos valores en una lista
    return list(kwargs.values())


## ejercicio 3 

def describir_persona(nombre, **kwargs):
    # Imprime el título con el nombre de la persona
    print(f"Características de {nombre}:")
    
    # Recorre cada argumento recibido en **kwargs
    # clave = nombre del atributo, por ejemplo color_ojos
    # valor = valor del atributo, por ejemplo azules
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")