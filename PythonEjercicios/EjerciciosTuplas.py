
numeros= [1,2,3,4,5]


def calcular_estadisticas(numeros):
    numeros.sort()
    numeroMinimo = numeros[0]
    numeroMaximo = numeros[4]
    numeroMedio = sum(numeros)/len(numeros)

    tupla = (numeroMinimo, numeroMaximo, numeroMedio)

    return tupla

print(calcular_estadisticas(numeros))

def distancia(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 1/2

print(distancia((1,2), (6,7)))

def analizar_texto(texto):
    contadorLetras = 0
    contadorPalabras = 0
    texto = texto.split(" ")
    for palabra in texto:
        contadorPalabras += 1
        for letra in palabra:
            contadorLetras += 1

    tupla2 = (contadorLetras, contadorPalabras,texto[0])
    return tupla2


print(analizar_texto("Hola mundo"))


