#Ejercicio2

def calculaPosicion(n,datos):
    posiciones = []
    posicion = 0
    for dato in datos:
        posicion = posicion + 1
        if dato == n:
            posiciones.append(posicion)
    if len(posiciones) == 0:
        return -1

    return posiciones

print(calculaPosicion(3,(2,4,7,3,8,0,3,1,5,7)))

def calculaPosicionAñade(n,datos):
    posiciones = []
    posicion = 0
    for dato in datos:
        posicion = posicion + 1
        if dato == n:
            posiciones.append(posicion)
    if len(posiciones) == 0:
        datos.insert(n-1,n)
        #datos[n-1] = n
        return datos

    return posiciones

print(calculaPosicionAñade(3,[2,4,7,8,0,1,5,7]))