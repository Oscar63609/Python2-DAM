import csv

with open("productos.csv","r") as archivo:
    producto = input("Introduce el prudcuto que quieres comprar : ")
    producto.lower().strip()
    unidades = input("Ahora introduce la cantidad de unidades que quieres comprar de ese producto :")
    print(producto)
    print(unidades)
    a = csv.DictReader(archivo, delimiter=';')
    for row in a:
        if producto not in row['producto']:
            print("Producto NO ENCONTRADO")
            break
        else:
            if int(unidades) > int(row['stock']):
                print("Producto SIN STOCK")
                break
            else:
                totalCompra = float(unidades) * float(row['precio'])
                print("Producto ENCONTRADO - Producto: ",str(producto))
                print("Precio Total: " ,str(totalCompra))
                resta = int(row['stock']) - int(unidades)
                row["stock"] = str(resta)
                break
