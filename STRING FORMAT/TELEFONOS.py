# cadena = "Pedro*111111111;Anabel*222222222;Jacinta*333333333;Andres*444444444;"
# 1) mostrar
# Pedro     111111111
# Anabel    222222222
# Jacinta   333333333
# Andres    444444444
# 2) Si la cadena esta ordenada, insertar un nuevo contacto, de froma ordenada crecientemente
# 3) Si la cadena no esta ordenada, ordenarla por nombres de forma creciente
# contacto = "Pedro*111111111"
# nombre = "Pedro"
# tfn = "111111111"
print("1)")
cadena = "Agosto*+00 123 45 67 89;Kp*+00 234 56 78 91;Agente*+00 345 67 89 12;Hachiko*+00 456 78 91 23;"
contacto = ""
datos = ""
for i in range(cadena.count(";")):
    if i == 0:
        inicio = 0
        final = cadena.find(";")
    else:
        inicio = final + 1
        final = cadena.find(";", inicio)
    contacto = cadena[inicio:final]
    nombre = contacto[:contacto.find("*")]
    tfn = contacto[contacto.find("*") + 1:]
    datos += "{:20}{:>15}\n".format(nombre, tfn)
print(datos)

# 2) si la cadena està ordenada, inserir un nou contacte, de forma ordenada creixentment
print("2)")
cadena = "Agente*+00 345 67 89 12;Agosto*+00 123 45 67 89;Hachiko*+00 456 78 91 23;Kp*+00 234 56 78 91;"
contacto_insertar = "Gulio*+00 000 00 00 00"
contacto = ""
datos = ""
longitud_inicial = len(cadena)
for i in range(cadena.count(";")):
    if i == 0:
        inicio = 0
        final = cadena.find(";")
    else:
        inicio = final + 1
        final = cadena.find(";", inicio)
    contacto = cadena[inicio:final]
    nombre = contacto[:contacto.find("*")]
    # tfn = contacto[contacto.find("*")+1:]
    # datos += "{:20}{:>15}\n".format(nombre, tfn)
    if contacto_insertar < contacto:
        cadena = cadena[:inicio] + contacto_insertar + ";" + cadena[inicio:]
        break
if longitud_inicial == len(cadena):
    cadena += contacto_insertar + ";"
print(cadena)

# 3)si la cadena no està ordenada, ordenar-la per noms de forma creixent
print("\n3)")
cadena = "Agosto*+00 123 45 67 89;Kp*+00 234 56 78 91;Agente*+00 345 67 89 12;Hachiko*+00 456 78 91 23;"
nueva_cadena = ""
contacto = ""
datos = ""
for i in range(cadena.count(";")):
    if i == 0:
        inicio = 0
        final = cadena.find(";")
    else:
        inicio = final + 1
        final = cadena.find(";", inicio)
    contacto = cadena[inicio:final]
    nombre = contacto[:contacto.find("*")]
    longitud_inicial = len(nueva_cadena)
    for j in range(nueva_cadena.count(";")):
        if j == 0:
            nuevo_inicio = 0
            nuevo_final = nueva_cadena.find(";")
        else:
            nuevo_inicio = nuevo_final + 1
            nuevo_final = nueva_cadena.find(";", nuevo_inicio)
        nuevo_contacto = nueva_cadena[nuevo_inicio:nuevo_final]
        nuevo_nombre = nuevo_contacto[:nuevo_contacto.find("*")]
        if nombre < nuevo_nombre:
            nueva_cadena = nueva_cadena[:nuevo_inicio] + contacto + ";" + nueva_cadena[nuevo_inicio:]
            break
    if longitud_inicial == len(nueva_cadena):
        nueva_cadena += contacto + ";"
cadena = nueva_cadena
print(cadena)
