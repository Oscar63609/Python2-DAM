import operaciones as op

#Ejercicio 1
op.info_argumentos("hola","adios")
op.divisibles3(3,4,5,6,7,8)
op.histograma(2,7,5)

#Ejrcicio2
print(op.coste_envio(5))
print(op.coste_envio(5,4))
print(op.coste_envio(5,envio_urgente=True))
print(op.coste_envio(2,6,envio_urgente=True))

#Ejercicio3
try:
    horas = int(input("Introduce las horas"))
    minutos = int(input("Introduce los minutos"))
    segundos = int(input("Introduce los segundos"))

    if horas > 24 and horas < 1:
        raise TypeError("Horas no es valido")

    if minutos > 59 or minutos < 1:
        raise TypeError("Minutos no es valido")

    if segundos > 59 or segundos < 1:
        raise TypeError("Segundos no es valido")

    print(op.convertir_segundos(horas,minutos,segundos))

except ValueError as e:
    print("Alguno de los valores introducido es incorrecto")
