with open("log.txt", "r") as fichero:
    contadorEliminados = 0
    contador = 0
    lineas = ""
    for linea in fichero:
        if linea.startswith("#") or linea.startswith("\n"):
            contadorEliminados += 1
        else:
            contador += 1
            lineas = lineas + linea
    open("log_limpio.txt", "w").write(lineas)
    print("Lineas eliminadas: " + str(contadorEliminados))
    print("Lineas introducidas en el nuevo fichero: " + str(contador))
