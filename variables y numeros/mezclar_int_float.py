# Cuando operas un int con un float, el resultado siempre es float. Python "promueve" el int a float automáticamente.
print(5 + 2.0)     # 7.0   (int + float = float)
print(10 * 0.5)    # 5.0   (int * float = float)
print(8 - 3.5)     # 4.5   (int - float = float)

# Verificar el tipo
resultado = 10 + 5.0
print(resultado)           # 15.0
print(type(resultado))     # <class 'float'>
#regla int + int = int (excepto división) • float + float = float • int + float = float. Python siempre elige el tipo más "amplio".

