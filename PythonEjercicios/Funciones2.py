try:

    def caculoNotas(nota):
        if nota < 0 or nota > 10:
            raise ValueError
        elif nota < 5:
            return "Suspenso."
        elif nota < 7:
            return "Aprobado."
        elif nota < 9:
            return "Notable."
        else:
            return "Sobresaliente."


    nota = float(input("Introduce una nota (0-10): "))
    print(caculoNotas(nota))
except ValueError:
    print("Error: introduce un número decimal válido.")
