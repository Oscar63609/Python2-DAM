try:
    def calculoSalario(horas, rate):
        salario = horas * rate
        return salario

    def salarioExtra(horas, rate):
        extra = horas - 40
        rateExtra = rate * 1.5
        salario = (40 * rate) + (extra * rateExtra)
        return salario

    horas = int(input("Ingresa la cantidad de horas: "))
    rate = float(input("Ingresa lo que te pagan por hora : "))
    if horas < 0 or rate < 0:
        raise ValueError
    elif horas <= 40:
        print(calculoSalario(horas, rate))
    elif horas > 40:
        print(salarioExtra(horas, rate))

except ValueError as e:
    print("Error: numero no valido",e)

