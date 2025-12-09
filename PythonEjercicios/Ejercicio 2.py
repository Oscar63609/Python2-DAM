try:
    numeros = 0
    mayor = 0
    medio = 0
    while True:

        precio = float(input("Ingrese el precio: "))

        if precio < 0:
            print("Error: el precio debe ser mayor a 0")
            continue
        elif precio == 9999.99:
            break
        elif precio > 10:
            numeros += 1
            medio = medio + precio
            print( "Total de precios introducidos ", medio)
            print(precio," es mayor a 10")
        elif precio == 10:
            numeros += 1
            medio = medio + precio
            print( "Total de precios introducidos ", medio)
            print(precio," es igual a 10")
        elif precio < 10:
            continue

        if mayor < precio:
            mayor = precio

        print("El precio mas alto por ahora es: ", mayor)


    print("El precio mas alto es: ", mayor)
    print(f"Hay {numeros} que son mayores o iguales que 10")
    print("El precio medio de todos los introducidos es: ", medio/numeros)

except ValueError as e:
    print("Error : ",e)