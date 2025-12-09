#Ejer 1
import random

try:
    aleatorio = random.randint(1, 100)
    while True:
        def adivinarNumero(numero):
            if numero < aleatorio:
                return 1
            elif numero > aleatorio:
                return 2
            elif numero == aleatorio:
                return aleatorio

        numero = int(input("Ingresa un numero: "))
        match adivinarNumero(numero):
            case 1:
                print("Tu numero es menor")
                continue
            case 2:
                print("Tu numero es mayor")
                continue
            case aleatorio:
                print("Tu numero es correcto")
                print("El numero aleatorio era: ", aleatorio)
                break

except ValueError:
    print("Error: ",ValueError)

#Ejer 2
try:

    def comprobarPrimo(numero):
        for i in range(2, numero):
            if numero % i == 0:
                return False
            else:
                return True

    numero = int(input("Ingresa un numero para comprobar si es primo "))
    if comprobarPrimo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")

except ValueError:
    print("Error :",ValueError)

#Ejer 3
try:
    def cuentaAtras(cantidad):
        for i in range(cantidad,-1,-1):
            print(i, end=", ")

    numero = int(input("Ingrese el numero: "))
    cuentaAtras(numero)

except ValueError:
    print("El numero no es valido")

#Ejer 4
try:
    while True:
        print("-----Calculaadora-------------")
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingresa el segundo numero: "))

        print("1. + o suma")
        print("2. - o resta")
        print("3. - o multiplicacion")
        print("4. - o division")
        operacion = input("Ingresa una operacion: ")

        def calculadora(numero1, numero2, operacion):
            if operacion == "+" or operacion == "suma" or operacion == "1":
                return numero1 + numero2
            elif operacion == "-" or operacion == "resta" or operacion == "2":
                return  numero1 - numero2
            elif operacion == "*" or operacion == "multiplicacion" or operacion == "3":
                return numero1 * numero2
            elif operacion == "/" or operacion == "division" or operacion == "4":
                try:
                    return numero1 / numero2
                except ZeroDivisionError:
                    print("No se puede realizar la division por cero")

        print(calculadora(numero1, numero2, operacion))

        respuesta = input("¿Desa volver a realizar una operacion?(si/no)")
        if respuesta == "si":
            continue
        elif respuesta == "no":
            break
        else:
            while respuesta != "si" and respuesta != "no":
                print("Respuesta no valida")
                respuesta = input("¿Desa volver a realizar una operacion?(si/no)")


except ValueError:
    print("Error:", ValueError)

#Ejer 5
try:
    conT = 0
    def nPrimos(numero):
        if numero > 0:
            for num in range(2,numero):
                cont = 0
                for i in range (2,num):
                    if num % i == 0:
                        cont += 1
                    if cont <2:
                        print(str(num) + " es un numero primo")

    numero = int(input("Ingresa un numero hasta el que contar "))
    print(nPrimos(numero))
except ValueError:
    print("Error:", ValueError)

#Ejer 6
try:
    cantidad = int(input("Ingrese la cantidad a invertir: "))
    interes = int(input("Ingrese la cantidad de interes anuanl: "))
    años = int(input("La cantidad de años a invertir: "))

    interes = interes/100
    def invertir(cantidad, interes,años):
        for i in range(1,años + 1):
            ganado = cantidad * interes
            cantidad = cantidad + ganado
        return cantidad


    print("La contidad invertida es ", invertir(cantidad,interes,años), "en el año", años)


except ValueError:
    print("Error:", ValueError)

#Ejer 7
nombres = ["Maria","Fernando","Infanta","Jose","Eduardo"]

nombres2 = ["Javier","Jose","Maria","Elena","Fernando"]


def combinar(nombres, nombres2):
    combinaciones = 0
    combinados=[]
    for n in nombres:
        for n2 in nombres2:
            if n != n2:
                try:
                    combinados.append(n + " " + n2)
                    combinaciones += 1
                    if n == "Infanta" and n2 == "Elena" :
                        raise MiExcepcion
                except MiExcepcion as e:
                    combinados.append("IES en Galapagar con estudios de formacion profesional")
    return combinados

print(combinar(nombres,nombres2))

#Ejer 8
def multiplos():
    numero = 7
    multiplicador = 1
    multiplo = numero * multiplicador
    while multiplo < 80:
        multiplicador = multiplicador + 1
        multiplo = numero * multiplicador
    return multiplo

print("El primer multiplo de 7 mayor que 7 es ", multiplos())

#Ejer 9
try:

    def tablaMultiplicacion(numero):
        resultado = []
        for i in range(1,11):
            resultado.append(numero * i)
        return resultado


    numero = int(input("Introduce el numero del que quieres saber la tabla de multiplicaciones:  "))
    print("Tabla de multiplicaciones:\n",tablaMultiplicacion(numero))
except ValueError:
    print("Error: ",ValueError)