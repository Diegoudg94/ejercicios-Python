# metodo index index()
# "Hola" los indices se empiezan a contar desde cero
#  0123
# -4 -3 -4 -1 0
# sirve para conocer la posicion de un caracter
mi_texto ="Hola"
mi_texto.index("o")
print(mi_texto.index("o"))  

mi_texto1 ="Esta es una prueba"
resultado =mi_texto1[-4]
resultado1 =mi_texto1.index("s")
print(resultado)
print(resultado1)
palabra_completa =mi_texto1.index("prueba")
print(palabra_completa)
varias_veces = mi_texto1.index("a")
print(varias_veces)
apartirde = mi_texto1.index("a", 5)
print(apartirde)
resultado2 = mi_texto1.rindex("a") # es  para buscar al revez
print (resultado2)


