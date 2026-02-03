import csv
"""
#Ejercicio Avanzado 2
diccionario = {}
palabras = []
def contador_palabras(texto):
    contador = 0
    fichero = open(texto, 'r')
    palabras = fichero.read().replace('\n', ' ').split(" ")
    for palabra in palabras:
        if palabra not in diccionario:
            for palabra2 in palabras:
                if palabra == palabra2:
                    contador += 1
            diccionario[palabra] = contador
    return diccionario

print (contador_palabras('datos.txt'))

#Ejercicios CSV
with open("datos.csv", 'r') as fichero:
    cont = 0
    f = csv.reader(fichero)
    next(f)
    for linea in f:
        cont += 1
        print(linea , cont)

with open("datos.csv", 'r') as fichero:
    f = csv.DictReader(fichero)
    next(f)
    for linea in f:
        print(linea)
    fichero.seek(0)
    for linea in f:
        print(linea["Nombre"])
"""

#Ejercico 4 CSV
with open("notas.csv", 'r') as fichero:
    total = 0
    cont = 0
    f = csv.DictReader(fichero)
    next(f)
    for linea in f:
        cont += 1
        total += int(linea["Nota"])
        #total = total + linea["Nota"]
    media = total / cont
    print(media)

#Ejercicio 5 CSV
with open("productos.csv", 'w',newline="") as fichero:
    f = csv.writer(fichero)
    f.writerow(['Producto', 'Precio','Cantidad'])
    f.writerow(['Manzana','1.50','100'])
    f.writerow(["Banana","0.80","150"])
    f.writerow(["Naranja","0.90","120"])


#Ejercicio 6 CSV
with open("empleados.csv", 'r') as fichero:
    f = csv.DictReader(fichero)
    next(f)
    for linea in f:
        if int(linea["Salario"]) > 3000:
            print (linea)

estudiantes = [
    {'Nombre': 'Juan', 'Edad': '20', 'Grado': 'A'},
    {'Nombre': 'Ana', 'Edad': '22', 'Grado': 'B'},
    {'Nombre': 'Luis', 'Edad': '21', 'Grado': 'A'}
]
#Ejercicio 7 CSV
with open("estudiantes.csv", 'w',newline="") as fichero:
    f = csv.DictWriter(fichero, fieldnames=['Nombre','Edad','Grado'])
    f.writeheader()
    f.writerows(estudiantes)

