"""
# Actividad 1
cadena = "Pedro Sebastian;Anabel;Andres;Maria;"
aux = cadena.find(";")
for i in range(cadena.count(";")):
    if i == 0:
        print(cadena[:aux])
    else:
        ini = cadena.find(";", aux) + 1
        fin = cadena.find(";", ini)
        aux = fin
        print(cadena[ini:fin])

# Actividad 2
nombre_insertar = "Xavier"
cadena = "Anabel;Andres;Maria;Pedro Sebastian;"
aux = cadena.find(";")
len_ini = len(cadena)
for i in range(cadena.count(";")):
    if i == 0:
        ini = 0
        fin = aux
    else:
        ini = cadena.find(";", aux) + 1
        fin = cadena.find(";", ini)
        aux = fin
    nombre = cadena[ini:fin]
    if nombre_insertar < nombre :
        cadena = cadena[:ini] + nombre_insertar + ";" + cadena[ini:]
        break
if len(cadena) == len_ini:
    cadena = cadena + nombre_insertar + ";"
print(cadena)
"""
# Actividad 3
cadena = "Maria;Pedro Sebastian;Anabel;Andres;"
cadena_ordenada = ""
aux = cadena.find(";")
for i in range(cadena.count(";")):
    if i == 0:
        ini = 0
        fin = aux
    else:
        ini = cadena.find(";", aux) + 1
        fin = cadena.find(";", ini)
        aux = fin
    nombre = cadena[ini:fin]
    len_ini = len(cadena_ordenada)
    if len_ini == 0:
        cadena_ordenada = cadena_ordenada + nombre + ";"
    else:
        aux_ord = cadena_ordenada.find(";")
        for j in range(cadena_ordenada.count(";")):
            if j == 0:
                ini_ord = 0
                fin_ord = aux_ord
            else:
                ini_ord = cadena_ordenada.find(";", aux_ord) + 1
                fin_ord = cadena_ordenada.find(";", ini_ord)
                aux_ord = fin_ord
            nombre_cadena = cadena_ordenada[ini_ord:fin_ord]
            if nombre < nombre_cadena:
                cadena_ordenada = cadena_ordenada[:ini_ord] + nombre + ";" + cadena_ordenada[ini_ord:]
                break
        if len(cadena_ordenada) == len_ini:
            cadena_ordenada = cadena_ordenada + nombre + ";"
print(cadena_ordenada)