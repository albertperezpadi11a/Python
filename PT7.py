# Exercici 1
luckynum = 0
numFound = False
birthDate = input("Introdueix la teva data de naixament en format ddmmaaaa: ")
while not birthDate.isdigit():
    print("Format incorrecte")
else:
    while not numFound:
        for i in birthDate:
            luckynum = luckynum + int(i)
        birthDate = str(luckynum)
        if luckynum < 10:
            print("El número de la sort és {}".format(luckynum))
            numFound = True
        else:
            luckynum = 0

# Exercici 2
a = input("Digues un valor númeric: ")
while not a.isdigit() or int(a) < 1:
    print("Valor incorrecte")
    a = input("Digues un valor númeric: ")
else:
    a = int(a)
    b = input("Digues un exponent: ")
    while not b.isdigit():
        print("Valor incorrecte")
        b = input("Digues un exponent: ")
    else:
        b = int(b)
        aux = a
        if b == 0:
            a = 0
        else:
            for i in range(1, b):
                a = a * aux
        print("El resultat és {}".format(a))
