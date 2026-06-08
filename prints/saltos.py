print("Línea 1\nLínea 2\nLínea 3") #el salto de línea se representa con \n y hace que el texto siguiente se imprima en una nueva línea
print("A\tB\tC")
print("D\tE\tF")
print("G\tH\tI")
#el salto de tabulación se representa con \t y hace que el texto siguiente se imprima a una distancia determinada del texto anterior, creando una especie de tabla
print("Barra Normal: /")
print("Barra Invertida: \\")#la barra invertida se representa con \\ porque la barra normal se utiliza para otros propósitos en Python, como indicar el inicio de una secuencia de escape, por lo que para imprimir una barra invertida se necesita usar dos barras invertidas consecutivas.

print("""
    *****
   *     *
  *  ^ ^  *
  *  (o)  *
   *     *
    *****
""")
#el uso de triple comillas permite imprimir un bloque de texto tal como se escribe, incluyendo los saltos de línea y los espacios, lo que es útil para crear dibujos o diagramas en la consola.
## Repetir strings
print("ja" *3)#el operador de multiplicación (*) se puede usar para repetir un string un número determinado de veces. En este caso, "ja" se repetirá 3 veces, resultando en "jajaja".
print("beetlejuice " *  3)
print("hola " *5) # se deja espacio antes de cerrar la comilla para evitar que salga pegado el texto al repetirlo, por ejemplo, "hola" * 5 sin espacio resultaría en "holaholaholaholahola", mientras que "hola " * 5 resultaría en "hola hola hola hola hola ".
# acceder a caracteres individuales
#  los indices se extraen empezando de 0
# P Y T H O N
# 0 1 2 3 4 5
print("PYTHON"[0]) #P
print("Anita Lava la tina" [1], [4],[0]) 
#mas sencillo
frase = "Anita Lava la tina"
print(frase[1], frase[4], frase[0]) #n a A
#Indices negativos
# P Y T H O      N
# -6 -5 -4 -3 -2 -1

print("Negativo"[-1]) #o
print("Python"[-3]) #h
print("Python"[-6]) #P
print("Python"[-2]) #o
