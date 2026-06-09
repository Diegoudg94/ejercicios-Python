# ➕ ➖ ✖️ ➗ Las cuatro operaciones
# operador + - * /
#ejemplos
print(2+2)
print(2-2)
print(2*2)
print(2/2)

#Variables

precio = 100
cantidad = 5
total = precio * cantidad
print(total)    

# En Python 3, la división / siempre devuelve un float, incluso si el resultado es "exacto". 10 / 2 da 5.0, no 5.
# // division entera % modulo (resto) ** potencia
# ejemplos

print(100/3)
print(100//3)
print(100%3)
print(2**3) 

#Modulo resto sirve para saber que sobra despues de dividir
print(17 % 5)     # 2  (17 = 5*3 + 2)
print(10 % 3)     # 1  (10 = 3*3 + 1)
print(20 % 4)     # 0  (división exacta)

# ¿Es par o impar?
print(8 % 2)      # 0 → es par
print(7 % 2)      # 1 → es impar

#potencia  Eleva un número a una potencia. También funciona para raíces (usando decimales).
print(2 ** 3)     # 8      (2³ = 2×2×2)
print(5 ** 2)     # 25     (5² = 5×5)
print(10 ** 4)    # 10000  (10⁴)

# Raíz cuadrada (potencia 0.5)
print(16 ** 0.5)  # 4.0    (√16 = 4)
print(27 ** (1/3)) # 3.0    (∛27 = 3)