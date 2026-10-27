# Vamos a crear un programa que nos sirva como agenda telefónica.
# El programa empezará con un menú muy simple:
#
# 1)Nuevo Telefono
# 2)Mostrar agenda
# 3)Salir
# Opcion:
#
# Si clicamos una opción diferente, el programa nos avisará mostrando
# un mensaje que nos avise que la opción es incorrecta,
# y seguidamente volverá a mostrar el menú
#
#
# Si entramos en la opcion 1, nos pedirá un nombre y un teléfono, nos
# mostrará un mensaje de confirmación para guardar el nuevo contacto,
# y en caso que confirmemos, se añadirá el contacto a nuestra agenda,
# y seguidamente volverá a mostrar el menú
#
# Si entramos en la opción 3, nos mostrará la agenda en una tabla formateada correctamente
# ************Agenda************
# Nombre                     Tfn
# ******************************
# Nuria                777777777
# Andres               909090909
#
# Nos mostrará un mensaje del tipo "Enter to continue" que pausará el programa, y cuando
# presionemos intro volverá a mostrarnos el menú
#
# Si vamos a la opción 3, nos mostrará un mensaje del tipo:
# "Saliendo del programa", se quedará pausado con un mensaje del tipo
# "Enter to continue" y al presionar intro se terminará la ejecución del programa
menu = "Agenda telefonica\n\n1)Nuevo Telefono\n2)Mostrar Agenda\n3)Salir"
contacts = "Agenda".center(30, "*") + "\n" + "{:15}{:>15}\n".format("Nombre", "Tfn") + "*" * 30 + "\n"
close = False
while not close:
    print(menu)
    option = input("Opcion: ")
    if not option.isdigit():
        print("Opcion no numerica")
        input("Press Enter to continue...\n")
    elif int(option) not in range(1, 4):
        print("Opcion fuera de rangp")
        input("Press Enter to continue...\n")
    else:
        option = int(option)
        if option == 1:
            name = input("Introduce el nombre: ")
            phone = input("Introduce el telefono: ")
            confirmation = input("Quieres guardar el nuevo contacto? (Y/N) ")
            if confirmation == "Y" or confirmation == "y":
                contacts = contacts + "{:15}{:>15}\n".format(name, phone)
        elif option == 2:
            print("\n" + contacts)
        else:
            print("Saliendo del programa")
            input("Press Enter to continue...")
            close = True
