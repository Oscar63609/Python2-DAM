class Ejercicio1:
    nombres = ["Maria", "Fernando", "Infanta", "Jose", "Eduardo"]

    nombres2 = ["Javier", "Jose", "Maria", "Elena", "Fernando"]

    combinaciones = 0

    for n in nombres:
        print(n)
        for n2 in nombres2:
            if n != n2:
                print(n + " " + n2)
                combinaciones += 1
                try:
                    if n == "Infanta" and n2 == "Elena":
                        print((n + " " + n2), "- IES en Galapagar con estudios de formacion profesional")
                except TypeError as e:
                    print(e)

    for n in nombres2:
        print(n)
        for n2 in nombres:
            if n != n2:
                print(n + " " + n2)
                combinaciones += 1

    print("El numero total de combinaciones es ", combinaciones)



class Ejercicio2:
        numeros = 0
        mayor = 0
        medio = 0
        while True:
            try:

                precio = float(input("Ingrese el precio: "))

                if precio < 0:
                    print("Error el precio debe ser mayor a 0")
                    continue
                elif precio == 9999.99:
                    break
                elif precio > 10:
                    numeros += 1
                    medio = medio + precio
                    print("Total de precios introducidos ", medio)
                    print(precio, " es mayor a 10")
                elif precio == 10:
                    numeros += 1
                    medio = medio + precio
                    print("Total de precios introducidos ", medio)
                    print(precio, " es igual a 10")
                elif precio < 10:
                    continue

                if mayor < precio:
                    mayor = precio

                print("El precio mas alto por ahora es: ", mayor)

            except ValueError as e:
                print("Error : ", e)

        print("El precio mas alto es: ", mayor)
        print(f"Hay {numeros} numeros que son mayores o iguales que 10")
        print("El precio medio de todos los introducidos es: ", medio / numeros)



class Ejercicio3:
    print("La secuencia de Fibonacci es: ")
    fibonacci1 = 0
    fibonacci2 = 1
    print(fibonacci1)
    print(fibonacci2)
    for i in range(fibonacci2, 9):
        result = fibonacci1 + fibonacci2
        print(result)
        fibonacci1 = fibonacci2
        fibonacci2 = result