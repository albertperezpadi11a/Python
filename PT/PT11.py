# Exericic 1
valid = False
while not valid:
    name = input("Introdueix un nom d'usuari: ")
    if len(name) < 6:
        print("El nom d'usuari ha de contenir almenys 6 caràcters")
        input("Prem Enter per continuar...")
    elif len(name) > 12:
        print("El nom d'usuari no pot contenir més de 12 caràcters")
        input("Prem Enter per continuar...")
    elif not name.isalnum():
        print("El nom d'usuari pot contenir només lletres i números")
        input("Prem Enter per continuar...")
    else:
        valid = True

# Exercici 2
valid = False
alpha = False
lower = False
upper = False
num = False
while not valid:
    password = input("Introdueix una contrasenya: ")
    for char in password:
        if not char.isalnum():
            alpha = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        if char.isnumeric():
            num = True
    if len(password) < 8 or password.find(" ") > 0 or not alpha or not lower or not upper or not num:
        print("La contrasenya no és segura.")
        input("Prem Enter per continuar...")
    else:
        valid = True

# Exercici 3
passwd_valid = False
user_valid = False
alpha = False
lower = False
upper = False
num = False
while not user_valid or not passwd_valid:
    name = input("Introdueix un nom d'usuari: ")
    if len(name) < 6:
        print("El nom d'usuari ha de contenir almenys 6 caràcters")
        input("Prem Enter per continuar...")
    elif len(name) > 12:
        print("El nom d'usuari no pot contenir més de 12 caràcters")
        input("Prem Enter per continuar...")
    elif not name.isalnum():
        print("El nom d'usuari pot contenir només lletres i números")
        input("Prem Enter per continuar...")
    else:
        user_valid = True
    if user_valid:
        password = input("Introdueix una contrasenya: ")
        for char in password:
            if not char.isalnum():
                alpha = True
            if char.islower():
                lower = True
            if char.isupper():
                upper = True
            if char.isnumeric():
                num = True
        if len(password) < 8 or password.find(" ") > 0 or not alpha or not lower or not upper or not num:
            print("La contrasenya no és segura.")
            input("Prem Enter per continuar...")
        else:
            passwd_valid = True
