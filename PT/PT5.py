#Exercici 1
num = int(input("Digues un número: "))
if num % 2 == 0:
    print("Es parell")
else:
    print("Es senar")

#Exercici 2
workedh = int(input("Digues les hores treballades: "))
installedm = int(input("Digues els metres instalats: "))
gprice = workedh * 30 + installedm * 0.5
price = gprice + gprice * 0.21
print(f"El preu brut és {gprice:.2f}€\nEl preu amb IVA és {price:.2f}€")

#Exercici 3
num1 = int(input("Digues un número: "))
num2 = int(input("Digues un número: "))
num3 = int(input("Digues un número: "))
if num1 < num2 and num2 < num3:
    print("Números en ordre")
else:
    print("Números desordenats")

#Exercici 4
year = int(input("Digues un any per saber si és de trespàs: "))
if year%4 == 0 and (not year%100 == 0 or year%400 == 0):
    print("Any de trespàs")
else:
    print("Any normal")

#Exercici 5
h = int(input("Numeros d'hores setmanals treballades a la setmana: "))
ph = int(input("Preu per hora: "))
extrah = False
if h <= 35:
    price = ph * h
else:
    h = h - 35
    price =  ph * h + (ph * h) * 0.5 + ph * 35
    extrah = True
if extrah:
    print(f"El preu és {price:.2f}€. Amb hores extres")
else:
    print(f"El preu és {price:.2f}€. Sense hores extres")

#Exercici 6
header = "=" * 31 + "\n" +\
         "= 1.- Euros a Dolars" + "\n" + \
         "= 2.- Euros a Yens" + "\n" + \
         "= 3.- Dolars a Euros" + "\n" + \
         "= 4.- Dolars a Yens" + "\n" + \
         "= 5.- Yens a Euros" + "\n" + \
         "= 6.- Yens a dolars" + "\n" + \
         "=" * 31 + "\n" +\
         "= Tria una opció de conversió =" + "\n" + \
         "=" * 31
print(header)
option = input()
if option == "1":
    euros = float(input("Quantitat Euros: "))
    dolars = euros * 1.11894
    print("{:.2f}$".format(dolars))
elif option == "2":
    euros = float(input("Quantitat Euros: "))
    yens = euros * 115.998
    print("{:.2f}¥".format(yens))
elif option == "3":
    dolars = float(input("Quantitat Dolars: "))
    euros = dolars / 1.11894
    print("{:.2f}€".format(euros))
elif option == "4":
    dolars = int(input("Quantitat Dolars: "))
    yens = dolars / 1.11894 * 115.998
    print("{:.2f}¥".format(yens))
elif option == "5":
    yens = float(input("Quantitat Yens: "))
    euros = yens / 115.998
    print("{:.2f}€".format(euros))
elif option == "6":
    yens = float(input("Quantitat Yens: "))
    dolars = yens / 115.998 * 1.11894
    print("{:.2f}$".format(dolars))
else:
    print("Opció incorrecta")
