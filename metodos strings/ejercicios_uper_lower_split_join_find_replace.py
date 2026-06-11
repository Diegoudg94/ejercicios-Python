#ejercicio1 cambiar texto a mayusculas 
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
resultado = frase.upper()
print(resultado)

lista = ["la", "legibilidad", "cuenta."]
resultado1 = " ".join(lista)
print(resultado1)

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea"
resultado2 = texto.replace("difícil", "fácil").replace("mala", "buena")
print(resultado2)   