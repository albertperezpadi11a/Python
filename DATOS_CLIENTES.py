cabecera = "Datos Clientes".center(47,"*") + "\n"+\
         "{:20}{:>5}  {:10}{:>10}\n".format("Nombre", "Edad", "DNI", "Tfn") +\
        "*"*47 + "\n"
lista = ""
#Primer articulo
nombre = input("Nombre: ")
edad = input("Edad: ")
dni = input("DNI: ")
telefono = input("Telefono: ")
lista = lista + "{:20}{:>5}  {:10}{:>10}\n".format(nombre, edad, dni, telefono)
print(cabecera + lista)
#Segundo articulo
nombre = input("Nombre: ")
edad = input("Edad: ")
dni = input("DNI: ")
telefono = input("Telefono: ")
lista = lista + "{:20}{:>5}  {:10}{:>10}\n".format(nombre, edad, dni, telefono)
print(cabecera + lista)
#Tercer Articulo
nombre = input("Nombre: ")
edad = input("Edad: ")
dni = input("DNI: ")
telefono = input("Telefono: ")
lista = lista + "{:20}{:>5}  {:10}{:>10}\n".format(nombre, edad, dni, telefono)
print(cabecera + lista)