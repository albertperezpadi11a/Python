x = input("Introduce un numero: ")
desc = ""
while not x.isdigit():
    print("Valor incorrecto")
    x = input("Introduce un numero: ")
else:
    x = int(x)
    x_original = x
    for i in range(1,x//2+1):
        cont = 0
        while x % i == 0:
            x = x // i
            cont = cont + 1
        if cont > 0:
            if desc == "":
                desc= "{}^{}".format(i,cont)
            else:
                desc = desc + "{}^{}".format(i,cont)
    print(desc)