# Ejercicio 1
def info_argumentos(*args):
    contador = 0
    for arg in args:
        contador += 1
        print(arg)
    print("Has pasado "+ str(contador) + " argumentos a la funcion")

def divisibles3(*args):
    for arg in args:
        if arg % 3 == 0:
            print(arg)

def histograma(*args):
    for arg in args:
        lista = []
        for i in range(0, arg):
            lista.append("*")
        print(lista)

#Ejrcicio 2
def coste_envio(peso,tarifa_base = 5,envio_urgente = False):
    if envio_urgente:
        for p in range(0,peso):
            tarifa_base = tarifa_base + 2
        precio_final = tarifa_base + (tarifa_base * (30/100))
    else:
        for p in range(0,peso):
            tarifa_base = tarifa_base + 2
        precio_final = tarifa_base
    return precio_final

#Ejercicio 3
def convertir_segundos(horas,minutos,segundos):
    horas_segundos = horas * 3600
    minutos_segundos = minutos * 60
    segundos_segundos = segundos

    return horas_segundos + minutos_segundos + segundos_segundos