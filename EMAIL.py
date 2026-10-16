valid = False
while not valid:
    email = input("Introduce el correo del email: ")
    if email.count("@") != 1:
        print("Sobran o falta el arroba")
    if email.find("@") == 0 or email.find("@") == len(email) - 1:
        print("Usuario o dominio vacios")