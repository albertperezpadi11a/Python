cabecera = "{:10}{:16}{:>10}\n".format("Dni","Nombre","Nota") + "Alumnos".center(36,"*") + "\n"
datos = ""

#Primera nota
dni = input("Dni: ")
nombre = input("Nombre: ")
nota = float(input("Nota: "))
datos = datos + "{:10}{:16}{:10.4f}\n".format(dni,nombre,nota)
print(cabecera + datos)

#Segunda nota
dni = input("Dni: ")
nombre = input("Nombre: ")
nota = float(input("Nota: "))
datos = datos + "{:10}{:16}{:10.4f}\n".format(dni,nombre,nota)
print(cabecera + datos)