#Python puede manejar numeros muy grandes o muy pequeños  usando notacion cientifica con e

print(1.e6)  #1000000.0  (1 × 10⁶)
print(2.5e8)     # 250000000.0

# Números pequeños
print(1e-3)      # 0.001  (1 × 10⁻³)
print(5e-6)      # 0.000005

# Enteros grandes (Python los maneja bien)
grande = 10 ** 100
print(type(grande))  # <class 'int'>

#🔢 Separador visual (guión bajo)
#Para números largos, puedes usar _ como separador visual. Python lo ignora.
# Más fácil de leer
poblacion = 8_000_000_000
precio = 1_500_000.50

print(poblacion)  # 8000000000
print(precio)     # 1500000.5