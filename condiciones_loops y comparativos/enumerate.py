# Enumerador 

#viejo metodo con indice 

mi_lista = ["a", "b", "c"]
indice = 0 #todos los indices van de cero
for item in mi_lista:
    print(indice, item)
    indice += 1

#nuevo metodo con enumerador 

mi_lista = ["a", "b", "c"]
for item in enumerate(mi_lista):
    print(item)

#mas sintetico y eficiente
mi_lista = ["a", "b", "c"]
for indice, item in enumerate(mi_lista):
    print(indice, item)

mi_lista = ["a", "b", "c"]
for indice, item in enumerate (range(50,55)):
    print(indice, item)

## Se puede hacer fuera de loops

mi_lista = ["a", "b", "c"]
mis_elementos = list(enumerate(mi_lista))
print(mis_elementos)


mi_lista = ["a", "b", "c"]
mis_elementos = list(enumerate(mi_lista))
print(mis_elementos[1][1])

