#reto 
# en una empresa los vendedores reciben comison del 13% de sus comisiones totales
# un programa que le pregunte su nombre y cuanto ha vendido
# el programa regresara nombre del vendedor y le dira cuanto ha ganado por sus comisions
# empieza preguntando cosas al usuario (input) se usaran variables los input se guardan como string 
# se deben convertir los int a floats 
vendedor = (input("Ingresa tu nombre "))
monto_vendido =  (input("Cuanto has vendido "))
monto_vendido = float(monto_vendido)
print(f"Hola {vendedor} has vendido {monto_vendido} tu comision es de {monto_vendido * 0.13}")