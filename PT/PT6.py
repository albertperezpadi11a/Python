# Exercici 1
menu = "Calculadora\nMenu Principal\n\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n0 - Sortir\n\nOpció: "
close = False

while not close:
    option = input(menu)
    if not option.isdigit():
        print("Opció no númerica")
        input("Prem Enter per continuar...\n")
    elif int(option) < 0 or int(option) > 4:
        print("Opció fora de rang")
        input("Prem Enter per continuar...\n")
    else:
        option = int(option)
    if option == 1:
        num1 = input("Introdueix el primer número: ")
        while not num1.isdigit():
            print("Num1 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el primer número: ")
        num1 = int(num1)
        num2 = input("Introdueix el segon número: ")
        while not num2.isdigit():
            print("Num2 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el segon número: ")
        num2 = int(num2)
        result = num1 + num2
        print("El resultat de la suma és: ", result)
        input("Prem Enter per continuar...\n")
    elif option == 2:
        num1 = input("Introdueix el primer número: ")
        while not num1.isdigit():
            print("Num1 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el primer número: ")
        num1 = int(num1)
        num2 = input("Introdueix el segon número: ")
        while not num2.isdigit():
            print("Num2 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el segon número: ")
        num2 = int(num2)
        result = num1 - num2
        print("El resultat de la resta és: ", result)
        input("Prem Enter per continuar...")
    elif option == 3:
        num1 = input("Introdueix el primer número: ")
        while not num1.isdigit():
            print("Num1 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el primer número: ")
        num1 = int(num1)
        num2 = input("Introdueix el segon número: ")
        while not num2.isdigit():
            print("Num2 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el segon número: ")
        num2 = int(num2)
        result = num1 * num2
        print("El resultat de la multiplicació és: ", result)
        input("Prem Enter per continuar...\n")
    elif option == 4:
        num1 = input("Introdueix el primer número: ")
        while not num1.isdigit():
            print("Num1 ha de ser un número")
            input("Prem Enter per continuar...\n")
            num1 = input("Introdueix el primer número: ")
        num1 = int(num1)
        num2 = input("Introdueix el segon número: ")
        while not num2.isdigit() or int(num2) == 0:
            if num2 == "0":
                print("No es pot dividir per 0")
                input("Prem Enter per continuar...\n")
            else:
                print("Num2 Ha de ser un número")
                input("Prem Enter per continuar...\n")
            num2 = input("Introdueix el segon número: ")
        num2 = int(num2)
        result = num1 / num2
        print("El resultat de la divisió és: ", result)
        input("Prem Enter per continuar...\n")
    elif option == 0:
        input("Sortint del programa")
        close = True

# Exercici 2
mult10 = False
num = 0
while not mult10:
    num = int(input("Introdueix un número multiple de 10: "))
    if num % 10 == 0:
        mult10 = True
    else:
        print(f"{num} no és un múltiple de 10. Torna-ho a intentar.\n")
powerof = 0
aux = num
while aux > 0 and aux % 10 == 0:
    powerof = powerof + 1
    aux = aux // 10
print("{} per 10 elevat a {}".format(aux, powerof))

# Exercici 3
bacteria = 1
minutes = 0
while bacteria < 10000000:
    bacteria = bacteria * 2
    minutes = minutes + 3
hours = minutes // 60
minutes = minutes % 60
print("La bacteria ha tardat {} hores i {} minuts en assolir la xifra mortal".format(hours,minutes))

# Exerici 4
num = 0
for i in range(1, 1001):
    if i % 7 == 0:
        num = num + 1
print("Hi ha {} números múltiples de 7 entre 1 i 1000".format(num))

# Exercici 5
num = 0
for i in range(1, 101):
    num = num + i
print("La suma dels 100 primers números és: {}".format(num))

# Exercici 6
quantity = int(input("Introdueix quants números vas a introduir: "))
min_num = 0
max_num = 0
tsum = 0
for i in range(1, quantity + 1):
    num = float(input("Introdueix el número {}: ".format(i)))
    if i == 1:
        min_num = num
        max_num = num
        tsum = tsum + num
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    tsum = tsum + num
average = tsum / quantity
print("El número més petit és: {}, el més gran és: {} i la mitjana és: {:.2f}".format(min_num, max_num, average))

# Exercici 7
width = int(input("Amplada del rectangle: "))
length = int(input("Alçada del rectangle: "))
for i in range(length):
    if i == 0 or i == length - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")

# Exercici 8
num = int(input("Dona'm un número: "))
print("Els divisors de {} són:".format(num), end=" ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

# Exercici 9
quantity = int(input("Quants números vas a introduir? "))
negatives = 0
print()
for i in range(1, quantity + 1):
    num = int(input("Dona'm el número {}: ".format(i)))
    if num < 0:
        negatives = negatives + 1
print("\nHas escrit {} números negatius.".format(negatives))

# Exercici 10
for i in range(1, 11):
    print("{:<10}".format(i), end="")
print()
for i in range(2, 21, 2):
    print("{:<10}".format(i), end="")
print()
for i in range(20, 39, 2):
    print("{:<10}".format(i), end="")
print()
for i in range(10, 31, 4):
    print("{:<10}".format(i), end="")
print()
for i in range(40, -1, -5):
    print("{:<10}".format(i), end="")
