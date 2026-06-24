#Ejercicio1

# Definimos una función llamada devolver_distintos
# que recibe 3 números como parámetros
def devolver_distintos(num1, num2, num3):

    # Guardamos en una variable la suma de los 3 números
    suma = num1 + num2 + num3

    # Si la suma es mayor a 15,
    # devolvemos el número más grande de los 3
    if suma > 15:
        return max(num1, num2, num3)

    # Si la suma es menor a 10,
    # devolvemos el número más pequeño de los 3
    elif suma < 10:
        return min(num1, num2, num3)

    # Si la suma está entre 10 y 15, incluidos,
    # devolvemos el número intermedio
    else:
        # Para encontrar el intermedio:
        # a la suma total le quitamos el mayor y el menor
        # lo que sobra es el número de en medio
        return suma - max(num1, num2, num3) - min(num1, num2, num3)


# Llamamos a la función y le pasamos 3 números
resultado = devolver_distintos(4, 234, 6)

# Mostramos en pantalla el resultado que devuelve la función
print(resultado)


### ejercicio 2

# Definimos una función llamada letras_unicas
# que recibe una palabra como parámetro
def letras_unicas(palabra):

    # Convertimos la palabra en un set
    # El set elimina automáticamente las letras repetidas
    letras = set(palabra)

    # Ordenamos las letras únicas en orden alfabético
    # sorted() devuelve una lista ordenada
    letras_ordenadas = sorted(letras)

    # Devolvemos la lista de letras únicas y ordenadas
    return letras_ordenadas


# Llamamos a la función y le pasamos la palabra "entretenido"
resultado = letras_unicas("entretenido")

# Mostramos en pantalla el resultado
print(resultado)


### ejercio 3

# Definimos una función que puede recibir cualquier cantidad de números
# Para eso usamos *args
def ceros_consecutivos(*args):

    # Recorremos los índices desde 0 hasta el penúltimo número
    # Usamos len(args) - 1 porque vamos a comparar cada número con el siguiente
    for i in range(len(args) - 1):

        # Revisamos si el número actual es 0
        # y si el número que sigue también es 0
        if args[i] == 0 and args[i + 1] == 0:

            # Si encontramos dos ceros seguidos, devolvemos True
            return True

    # Si termina el ciclo y nunca encontró dos ceros seguidos,
    # devolvemos False
    return False


# Ejemplo 1: aquí sí hay dos ceros consecutivos
resultado = ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5)
print(resultado)  # True


# Ejemplo 2: aquí hay varios ceros, pero ninguno está pegado a otro cero
resultado = ceros_consecutivos(6, 0, 5, 1, 0, 3, 0, 1)
print(resultado)  # False


#ejercicio 4

def contar_primos(num):
    #creacion de un contador para guardar cuantos primos encontramos
    cantidad_primos = 0
    #recorremos numeros desde el 2 hasta num
    #empezamos del 2 porque 0 y 1 no son primos
    for numero in range(2,num+1):
        # al inicio asumimos que el numero si es primo
        es_primo =True
        #revisamos si el numero se puede dividir entre otro numero
        # que no se 1 ni el mismo
        for divisor in range(2,numero):
            #si el residuo es 0 significa que la division es exacta
            # entonces el numero no es primo
            if numero % divisor == 0:
                es_primo = False
                break
            # si despues de revisar divisodres sigue siendo primo
            if es_primo:
                cantidad_primos += 1
                #revuelve la cantidad total de primos
    return cantidad_primos
resultado = contar_primos(20)
print("cantidad de primos,", resultado)