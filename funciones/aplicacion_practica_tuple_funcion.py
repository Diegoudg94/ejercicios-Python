# ==========================================
# LISTAS CON TUPLAS
# ==========================================

# Esta lista contiene tuplas.
# Cada tupla tiene 2 datos:
# 1. El nombre del café
# 2. El precio del café

lista_cafe = [
    ("Capuccino", 1.5),
    ("Expresso", 1.2),
    ("Moka", 1.9)
]


# ==========================================
# PRIMERA FORMA
# Recorrer la lista completa
# ==========================================

# elemento representa cada tupla completa
for elemento in lista_cafe:
    print(elemento)

# Salida:
# ("Capuccino", 1.5)
# ("Expresso", 1.2)
# ("Moka", 1.9)


# ==========================================
# SEGUNDA FORMA
# Desempaquetar la tupla
# ==========================================

# Como cada tupla tiene 2 datos, podemos separarlos así:
# c = nombre del café
# p = precio del café

for c, p in lista_cafe:
    print(c)

# Aquí solo imprimimos el nombre del café
# porque estamos usando print(c)


# ==========================================
# FUNCIÓN PARA BUSCAR EL CAFÉ MÁS CARO
# ==========================================

def cafe_mas_caro(lista):

    # Esta variable guarda el precio más alto encontrado hasta ahora
    # Empezamos en 0 porque todavía no hemos revisado ningún café
    precio_mayor = 0

    # Esta variable guardará el nombre del café más caro
    cafe_mas_caro = ""

    # Recorremos la lista separando cada tupla en:
    # c = café
    # p = precio
    for c, p in lista:

        # Si el precio actual es mayor que el precio_mayor,
        # entonces encontramos un café más caro
        if p > precio_mayor:

            # Actualizamos el precio mayor
            precio_mayor = p

            # Guardamos el nombre del café más caro hasta ahora
            cafe_mas_caro = c

    # Al final devolvemos el café más caro y su precio
    return (cafe_mas_caro, precio_mayor)


# Llamamos la función y mostramos el resultado completo
print(cafe_mas_caro(lista_cafe))


# ==========================================
# GUARDAR EL RESULTADO EN VARIABLES
# ==========================================

# La función devuelve una tupla:
# ("Moka", 1.9)

# Podemos guardar cada parte en una variable:
# cafe guarda "Moka"
# precio guarda 1.9
cafe, precio = cafe_mas_caro(lista_cafe)

# Mostramos el resultado de forma más clara
print(f"El café más caro es {cafe} y su precio es {precio}")