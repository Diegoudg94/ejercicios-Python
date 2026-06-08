# input palablra clave input "se pide el dato al usuario"
#ejemplo de input
print(input("¿Cuál es tu nombre?")) #se muestra el mensaje y se espera a que el usuario escriba algo y presione enter, lo que escriba se mostrará en pantalla
print(input("¿Dime tu apellido?")) #se muestra el mensaje y se espera a que el usuario escriba algo y presione enter, lo que escriba se mostrará en pantalla

print  ("tu nombre es " + input("Cual es tu nombre?")) #se muestra el mensaje y se espera a que el usuario escriba algo y presione enter, lo que escriba se mostrará en pantalla junto con el mensaje "tu nombre es "
print  ("tu nombre es " + input("Cual es tu nombre?"), "y tu apellido es " + input("Cual es tu apellido?")) #se muestra el mensaje y se espera a que el usuario escriba algo y presione enter, lo que escriba se mostrará en pantalla junto con el mensaje "tu nombre es " y "y tu apellido es "
print("¿qué estas estudiando? " + input()) #se muestra el mensaje y se espera a que el usuario escriba algo y presione enter, lo que escriba se mostrará en pantalla junto con el mensaje "¿qué estas estudiando? "con el mensaje "¿qué estas estudiando? " y lo que escriba el usuario
print("En que pais vives? " + input()) #se muestra el mensaje y se espera a que el usuario escriba algo y presione enter, lo que escriba se mostrará en pantalla junto con el mensaje "En que pais vives? "con el mensaje "En que pais vives? " y lo que escriba el usuario
# Con mensaje (lo más común)
print(input("Escribe algo: "))

# Sin mensaje (solo espera que escribas)
print(input())

# ejemplos de concatenacion

# Bienvenida
print("Bienvenido a " + input("¿A qué ciudad viajas? "))

# Despedida
print("Hasta luego, " + input("Tu nombre: ") + ". ¡Vuelve pronto!")

# Confirmación
print("Tu correo es: " + input("Email: "))

print("¡Hola, " + input("Tu nombre: ") + " de " + input("Tu ciudad: ") + "!")