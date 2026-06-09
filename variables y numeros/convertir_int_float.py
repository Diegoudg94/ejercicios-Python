# de float a int
# usa int () para convertir un float a entero, OJO trunca decimales no redondeo
print(int(3.7))    # 3  (no redondea, trunca)
print(int(3.2))    # 3
print(int(9.99))   # 9  (¡no es 10!)
print(int(-2.8))   # -2 (hacia el cero)
#  De int a float
# Usa float() para convertir un entero a decimal. Agrega .0 al final.
print(float(5))     # 5.0
print(float(100))   # 100.0
print(float(-7))    # -7.0

# 📝 Convertir desde texto Puedes convertir strings que contengan números válidos.

# String a int
print(int("42"))      # 42
print(int("-15"))     # -15

# String a float
print(float("3.14"))  # 3.14
print(float("100"))   # 100.0

# Útil con input()
edad = int(input("Tu edad: "))
precio = float(input("Precio: "))
