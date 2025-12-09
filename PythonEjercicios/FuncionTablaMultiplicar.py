

def tablaMultiplicacion(numero,hasta = 10):
    resultado=[]
    for i in range(1,hasta+1):
        resultado.append(numero*i)
    return resultado
print(tablaMultiplicacion(numero=2))