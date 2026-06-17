# ==========================================
# APUNTES: MIN Y MAX EN PYTHON
# ==========================================

# min() sirve para obtener el valor menor
# max() sirve para obtener el valor mayor


# ==========================================
# EJEMPLO 1
# Buscar el menor y mayor entre varios números
# ==========================================

# min() devuelve el número más pequeño
menor = min(58, 96, 72, 64)
print(menor)

# max() devuelve el número más grande
mayor = max(58, 96, 72, 64)
print(mayor)


# ==========================================
# EJEMPLO 2
# Usar min() y max() con una lista
# ==========================================

# Lista de números
lista = [58, 96, 72, 64]

# Imprimimos la lista completa
print(lista)

# Imprimimos el número menor de la lista
print(min(lista))

# Imprimimos el número mayor de la lista
print(max(lista))

# Mostramos el menor y el mayor dentro de un texto
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")


# ==========================================
# EJEMPLO 3
# Usar min() y max() con strings en una lista
# ==========================================

# Lista de nombres
nombres = ["Juan", "Pablo", "Alicia", "Carlos"]

# Con strings, Python compara alfabéticamente
# min() devuelve el que aparece primero en orden alfabético
print(min(nombres))

# max() devuelve el que aparece después en orden alfabético
print(max(nombres))


# ==========================================
# EJEMPLO 4
# Usar min() con una palabra
# ==========================================

# Variable con un nombre
nombre = "Carlos"

# min() busca la letra menor según el orden interno de Python
# OJO: las letras mayúsculas se evalúan antes que las minúsculas
print(min(nombre))


# Convertimos todo a minúsculas con lower()
# Así comparamos las letras de forma más normal
nombre = "Carlos"
print(min(nombre.lower()))


# ==========================================
# EJEMPLO 5
# Error común con diccionarios
# ==========================================

# Esto NO es un diccionario, es un set de strings
di = {"c1: 45", "c2: 3"}

# Aquí min() y max() comparan los textos completos
print(min(di))
print(max(di))


# ==========================================
# EJEMPLO 6
# Usar min() y max() correctamente con diccionarios
# ==========================================

# Creamos un diccionario con claves y valores numéricos
di = {"c1": 45, "c2": 3}

# .values() obtiene solo los valores del diccionario: 45 y 3
# min() obtiene el valor más pequeño
print(min(di.values()))

# max() obtiene el valor más grande
print(max(di.values()))