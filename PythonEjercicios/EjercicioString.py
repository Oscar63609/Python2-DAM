
#Ejercicio-- Crea un metodo que reciva como parametro una frase y que este cuente
#las vocales totales de la frase, ademas debera de preguntar por una vocal y cambiar todas
#las vocales de la frase por esa vocal
"""
def vocales(frase):
    vocal=0
    opcion_vocal = str(input("Elije que vocal quieres cambiar :\n"))

    while (opcion_vocal not in "aeiou"):
        opcion_vocal = str(input("Opcion de vocal no valida, vuelve a introducir otra vocal\n"))

    for letra in frase:
        if letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vocal = vocal + 1
            frase = frase.replace(letra,opcion_vocal)

    return "Nueva frase : "+ frase +"\nNumero total de vocales contadas:" + str(vocal)

print(vocales("El viento susurra secretos que nadie escucha, mientras la luna vigila con ojos de plata."))

#ejercicio(David Kallimoulline)
#Encontrar la ruta más corta y eficiente para visitar un conjunto
#de ciudades una sola vez, regresando al punto de partida,

#Ejercicio(Mario Sáez)
#Invertir las palabras que tengan mas de 5 letras

def invertir(palabra):
    if len(palabra) > 5:
        palabra = palabra[::-1]
        return palabra
    else:
        print("La palabra tiene menos de 5 letras")

print(invertir("Valladolid"))

#Ejercicio(Diego Scott)
#Crea un método:  correos_nombres(lista_correos)  que con los correos de la lista de correos genere dos listas,
# una con los nombres y otras con los dominios de todos los correos e imprimirlos
arrayCorreos=["barack.obama@nagger.com", "angela.merkel@pretzel.com", "emmanuel.macron@gabacho.com", "justin.trudeau@pokemon.com", "gorge.fl@lakof" ]
def correos(array):
    nombres = []
    dominio = []
    for palabra in array:
        arroba = palabra.find("@")
        nomb = palabra[:arroba]
        dom = palabra[arroba+1:]
        nombres.append(nomb)
        dominio.append(dom)
    return nombres, dominio

print(correos(arrayCorreos))
"""
#Ejercicio (Tobias)
#Haz un metodo que reemplace cada palabra con la primera letra en mayuscula y cuenta cuantas ‘e’ hay.
frase1 = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"
def meyusculas(frase):
    contador = 0
    frasefinal = " "
    palabras = frase.split()
    for palabra in palabras:
        mayuscula = palabra[0:1].upper()
        palabrafinal = mayuscula + palabra[1:]
        frasefinal = frasefinal +" " +palabrafinal

    for letra in frase:
            if letra== "e":
                contador += 1

    return frasefinal, contador

print(meyusculas(frase1))


