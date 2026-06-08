# Extraer partes (slicing)
# Puedes extraer una porción del string usando [inicio:fin]. El carácter en fin NO se incluye.
# P Y T H O N
# 0 1 2 3 4 5
print("PYTHON"[0:3]) #PYT
print("Mexico"[1:3]) #ex
print("Mexico"[2:]) #xico
#ejemplos practicos
# Extraer extensión de archivo
print("documento.pdf"[-4:]) # .pdf
#extraer codigo de un pais
print("+52 33 1234 5678" [:3]) #+52
# Extraer las primeras 5 letras
print("Bienvenidos al curso"[:5])
# → Bienv