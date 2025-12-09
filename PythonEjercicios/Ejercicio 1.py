nombres = ["Maria","Fernando","Infanta","Jose","Eduardo"]

nombres2 = ["Javier","Jose","Maria","Elena","Fernando"]

combinaciones = 0

for n in nombres:
    print(n)
    for n2 in nombres2:
        if n != n2:
            print(n +" "+ n2)
            combinaciones += 1
            if n == "Infanta" and n2 == "Elena" :
                print((n +" "+ n2),"- IES en Galapagar con estudios de formacion profesional")
            #Correccion
            #try:
                #print(n + " " + n2)
                #combinaciones += 1
                #if n == "Infanta" and n2 == "Elena" :
                    #raise MiException
            #catch MiExceptionas e:
                #print("IES en Galapagar con estudios de formacion profesional")


for n in nombres2:
    print(n)
    for n2 in nombres:
        if n != n2:
            print(n +" "+ n2)
            combinaciones += 1

print("El numero total de combinaciones es ", combinaciones)