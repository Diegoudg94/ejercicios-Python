# Método upper
texto = "Este es el texto de Diego"
resultado = texto.upper() #Este metodo pondra todo en mayusculas, final van a llevar un parentesis vacios pero aveces requieren info
print (resultado)

# Método upper
texto = "Este es el texto de Diego"
resultado = texto[2:8].upper() # este solo va a poner en mayusclas las letras del indice seleccionado 
print (resultado)

# Método lower
texto = "ESTE ES EL TEXTO DE DIEGO"
resultado = texto.lower() # Este metodo pondra en minusculas todo el texto seleccionado
print (resultado)

texto = "ESTE ES EL TEXTO DE DIEGO"
resultado = texto[2:8].lower() # Este metodo pondra en minusculas todo el texto seleccionado
print (resultado)

#metodo split 
#muestra una lista con cada palabra del string
texto = "Este es el texto de Diego"
resultado = texto.split() 
print (resultado)

texto = "Este es el texto de Diego"
resultado = texto.split("t") #se puede añadir criterios de separacion dentro del parentesis 
print (resultado)

# Método join

a = "aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print (e)   

#Metodo find sirve para buscar en que posicion del indice esta un caracter

texto = "Este es el texto de Diego"
resultado = texto.find("s") # Devolvera -1 cuando no encuentre nada 
print (resultado)

#Metodo replace #permite remplazar un string por otro
texto = "Este es el texto de Diego"
resultado = texto.replace("Diego", "todos")
#                          orig.     remplazo
print(resultado)