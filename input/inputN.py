# int() para números enteros
# Si necesitas hacer cálculos, convierte el texto a número con int().

print(input("Numero: ") + input("Otro numero: "))
# Esto concatenará los dos números como texto.
# Por ejemplo: "5" + "3" dará "53"

# Convertido con int(): suma como números
print(int(input("Numero: ")) + int(input("Otro numero: ")))

# float para decimales
# Para precios, medidas y temperaturas, usa float().
print(float(input("Precio: $ ")) * 1.16)

# Calculadora simple
print("Calculadora simple")
print("Resultado:", float(input("Primer numero: ")) + float(input("Segundo numero: ")))

# Calculadora de edad
print("Tu edad es:", 2026 - int(input("¿En qué año naciste? ")))

# Área de un rectángulo
print("El área del rectángulo")
print("Área:", float(input("Base: ")) * float(input("Altura: ")))