diccionario = {
    "Estudiante1":{
    "nombre": "Oscar",
    "apellido": "Perez",
    "año": 2002,
    "mascota": "perro"
    },
    "Estudiante2":{
        "nombre": "Diego",
        "apellido": "Perez",
        "año": 2005,
        "mascota": "perro"
    },
    "Estudiante3":{
        "nombre": "Jorge",
        "apellido": "Pablos",
        "año": 2002,
        "mascota": "perro"
    },
    "Estudiante4":{
        "nombre": "Pablos",
        "apellido": "Perez",
        "año": 2005,
        "mascota": "perro"
    }
}
"""
print(diccionario)

for x, obj in diccionario.items():
    print("\n" + x)

    for y in obj:
        print(y +" :",obj[y])
"""
alumnos = {
    "Estudiante1": {
        "Python" : 5,
        "PSP" : 4,
        "Itinerarios" : 6
    },
    "Estudiante2": {
        "Python" : 7,
        "PSP" : 2,
        "Itinerarios" : 8
    },
    "Estudiante3": {
        "Python" : 3,
        "PSP" : 8,
        "Itinerarios" : 5
    },
    "Estudiante4": {
        "Python" : 9,
        "PSP" : 7,
        "Itinerarios" : 4
    }
}

def correcion_notas(notas):
    for x, obj in notas.items():
        for y in obj:
            if obj[y] < 5:
                print("\n" + x + " Esta suspenso en " + y)
                print("Pero se le va a aprobar el modulo por un fallo ocurrido")
                obj[y] = 5

    for x, obj in notas.items():
        print("\n" + x)

        for y in obj:
            print(y + " :", obj[y])

correcion_notas(alumnos)

personajes ={
    "caballero":{
        "vida": 0,
        "defensa": 0,
        "alcance": 0,
        "ataque": 0
    },
    "guerrero":{
        "vida": 2,
        "defensa": 2,
        "alcance": 2,
        "ataque": 2
    },
    "arquero":{
        "vida": 0,
        "defensa": 0,
        "alcance": 0,
        "ataque": 0
    }
}

def balanceo_personajes(personajes):
    personajes["caballero"]["vida"] = 2 * personajes["guerrero"]["vida"]
    personajes["caballero"]["defensa"] = 2 * personajes["guerrero"]["defensa"]
    personajes["caballero"]["alcance"] = personajes["guerrero"]["defensa"] / 2
    personajes["caballero"]["ataque"] = personajes["guerrero"]["defensa"] / 2
    personajes["guerrero"]["alcance"] = personajes["guerrero"]["defensa"] * 2
    personajes["arquero"]["ataque"] = personajes["guerrero"]["ataque"]
    personajes["arquero"]["vida"] = personajes["guerrero"]["vida"]
    personajes["arquero"]["alcance"] = personajes["guerrero"]["defensa"] * 2
    personajes["arquero"]["alcance"] = personajes["guerrero"]["defensa"] / 2

balanceo_personajes(personajes)
print(personajes)

