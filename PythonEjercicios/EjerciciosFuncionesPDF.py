import math
import random



#----------------------------------
#Ejercicio 1
def saludar(nombre, saludo="Hola"):
    return saludo + " " + nombre

#print(saludar(nombre="Elena"))

#Ejercicio 2
def calcularPrecio(precio_base,iva = 21.0):
    precio_final= (precio_base * (iva/100)) + precio_base
    return precio_final

#precio = float(input("Introduce el preciodobre el qeu quieres calcular el iva: "))
#print(calcularPrecio(precio))

#Ejercicio 3
def crearUsuario(nombre, email, activo=True):
    resultado=[]
    if activo:
        resultado.append(nombre)
        resultado.append(email)
    return resultado

#print("Introduce el nombre y el email del usuario")
#nombre = input()
#email = input()
#print(crearUsuario(nombre, email))
#crearUsuario(nombre="Oscar", email="osacar@gmail.com")

#Ejercicio 4
#def formater_nombre(nombre,apellido,orden =nombre + " " + apellido ):



#Ejercicio 5
def calcularDescuento(precio_original, descuento=10):
    precio_final = precio_original * (descuento / 100)
    return precio_final

#print(calcularDescuento(precio_original=200))

#Ejercicio 6
#enteros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def filtrar_pares(lista):
    pares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
    return pares
#print(filtrar_pares(enteros))

#Ejercicio 7
def tablaMultiplicacion(numero,hasta = 10):
    resultado=[]
    for i in range(1,hasta):
        resultado.append(numero*i)
    return resultado
#print(tablaMultiplicacion(numero=2))

#----------------------------------------------------------------------
#Ejercicio Pizza -- tamaño porciones/ ingredinetes deben ser un argumento que sea una lista
def make_pizza(tamaño,*ingredientes):
    if not ingredientes:
        print("No se puede hacer una pizza sin ingredientes")
    else:
        print("Has hecho una pizza de " + str(tamaño) + " porciones")
        print("Cuyos ingredinetes son")
        print("\nIngredientes:")
        for ingrediente in ingredientes:
            print(ingrediente)

def ganador(*participantes):
    if not participantes:
        print("No se puede hacer una carrera sin participantes")
        return "Error"
    else:
        return participantes[random.randint(0,len(participantes)-1)]

def calcularFactorial(numero):
    resultado=1
    for i in range(1,numero+1):
        resultado*=i
    return resultado

def calcularFactorial2(numero):
    n = int(numero)
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*calcularFactorial2(n-1)

def calcularfFibonacci(numeros):
    n = int(numeros)
    if n<=1:
        return n
    else:
        return calcularfFibonacci(n-1) + calcularfFibonacci(n-2)

