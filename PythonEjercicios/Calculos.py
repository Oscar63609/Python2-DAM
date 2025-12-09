import math

#Ej 1
def calcularAreaCirculo(radio=8):
    resultado=math.pi * (radio**2)
    return resultado

def calcularAreaRectangulo(lado=8,altura=8):
    resultado=lado*altura
    return resultado

def calcularAreaTriangulo(base=8,altura=8):
    resultado=(base*altura)/2
    return resultado

#Ej 2
def precioEntrada(estudiante,edad,precio = 10):
    if estudiante and edad <= 18:
        return precio * 0.5
    else:
        return precio

#Ej 3
def multiplicador(*numeros):
    resultado=1
    for numero in numeros:
        resultado = numero * resultado
    return resultado

#Ej 4
def multiplicandoUnaSuma(multiplicacador,*numeros):
    resultado = 0
    for numero in numeros:
        resultado = numero + resultado

    resultado = resultado * multiplicacador
    return resultado

#Ej 5
def contarArgumentos(*argumentos):
    resultado = 0
    for argumento in argumentos:
        resultado = resultado + 1
    return resultado