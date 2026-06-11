# ==========================================
# ANALIZADOR DE TEXTO
# ==========================================

# Pedimos al usuario que escriba un texto
texto_usuario = input("Escribe un texto: ")

# Pedimos al usuario que escriba 3 letras sin espacios
letras_usuario = input("Escribe 3 letras sin espacios: ")

# Convertimos el texto y las letras a minúsculas
conversor_texto = texto_usuario.lower()
conversor_letras = letras_usuario.lower()

# Separamos las 3 letras elegidas por el usuario
letra_1 = conversor_letras[0]
letra_2 = conversor_letras[1]
letra_3 = conversor_letras[2]

# Contamos cuántas palabras tiene el texto
contador_palabras = len(conversor_texto.split())

# Obtenemos la primera y última letra del texto
primera_letra = conversor_texto[0]
ultima_letra = conversor_texto[-1]

# Invertimos el texto
al_reves = conversor_texto[::-1]

# Revisamos si la palabra "python" aparece en el texto
comprobacion = "python" in conversor_texto

# Diccionario para mostrar una respuesta clara según el booleano
diccionario = {
    True: "La palabra Python sí aparece en el texto",
    False: "La palabra Python no aparece en el texto"
}

# Mostramos los resultados al usuario
print(f"La letra '{letra_1}' aparece {conversor_texto.count(letra_1)} veces")
print(f"La letra '{letra_2}' aparece {conversor_texto.count(letra_2)} veces")
print(f"La letra '{letra_3}' aparece {conversor_texto.count(letra_3)} veces")

print(f"Tu texto tiene: {contador_palabras} palabras")
print(f"La primera letra es: {primera_letra}")
print(f"La última letra es: {ultima_letra}")
print(f"El texto invertido es: {al_reves}")

print(diccionario[comprobacion])