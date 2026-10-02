header = "Alumnos".center(50,"*") + "\n" + \
         "{:15}{:15}{:>5} {:10}\n".format("DNI","Nombre","Nota","Nota Boletin") + "*" * 50 + "\n"
body = ""

#Primera Nota
dni = input("Dame el dni: ")
name = input("Dame el nombre: ")
score = float(input("Dame la nota: "))
scorew = ""
if score < 5:
    scorew = "Suspendido"
elif score <= 6:
    scorew = "Aprovado"
elif score < 7:
    scorew = "Bien"
elif score < 9:
    scorew = "Notable"
else:
    scorew = "Excelente"
body = body + "{:15}{:15}{:5.2f} {:10}\n".format(dni, name, score, scorew)
print(header + body)

#Segunda Nota
dni = input("Dame el dni: ")
name = input("Dame el nombre: ")
score = float(input("Dame la nota: "))
scorew = ""
if score < 5:
    scorew = "Suspendido"
elif score <= 6:
    scorew = "Aprovado"
elif score < 7:
    scorew = "Bien"
elif score < 9:
    scorew = "Notable"
else:
    scorew = "Excelente"
body = body + "{:15}{:15}{:5.2f} {:10}\n".format(dni, name, score, scorew)
print(header + body)