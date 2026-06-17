#Consiste en si se cumple una condicion python ejecuta un codigo u otro
# IF si
#Elif si no pasa una ver si hay otra
#else si no
#
#if una_conicion:
 #   print(codigo_a)
#else:
#    print(codigo_b) 
# elif otra_condicion:
#    print(codigo_c)
#else:
#    print(codigo_d)

if True: 
    print("Es correcto")

if 10 > 9:
    print("10 es mayor que 9")

if 3>100:
    print("es correcto")
else:
    print("no es correcto")

mascota = "perro"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("no se que mascota tienes")


mascota = "conejo"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("no se que mascota tienes")


edad = 16
calificacion = 9
if edad >18:
    print("eres mayor de edad")
else:
    print ("eres menor de edad")
    if calificacion >= 6:
        print("aprobado")
    else:
        print("reprobado")  


