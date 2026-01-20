#Ejercicio 1

def cuentaVocales(cadena):
    vocal_a ="La vocal a aparece "+ str(cadena.count("a")) + " veces"
    vocal_e = "La vocal e aparece "+ str(cadena.count("e")) + " veces"
    vocal_i = "La vocal i aparece "+ str(cadena.count("i")) + " veces"
    vocala_o = "La vocal o aparece "+ str(cadena.count("o")) + " veces"
    vocale_u = "La vocal u aparece "+ str(cadena.count("u")) + " veces"

    return vocal_a +"\n" +vocal_e+"\n" + vocal_i+"\n" + vocala_o+"\n" + vocale_u


print(cuentaVocales("me duele el esternocleidomastoideo"))