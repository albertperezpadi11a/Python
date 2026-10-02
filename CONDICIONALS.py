#Exercici 1
num = int(input("Digues un numero negatiu o positiu: "))
if num >= 0:
    print(f"El valor absolut és {num}")
else:
    num = num * -1
    print(f"El valor absolut és {num}")

#Exercici 2
edat = int(input("Digues una edat: "))
if edat < 3:
    print("El preu és 2€")
elif edat < 10:
    print("El preu és 10€")
else:
    print("El preu és 25€")

#Exercici 3
edat = int(input("Digues una edat: "))
carnet = input("Digues si tens carnet d'estudiant(Y/N): ")
if edat < 3:
    preu = 2
elif edat < 10:
    preu = 10
else:
    preu = 25
if carnet == "Y" or carnet == "y":
    preu = preu - preu*0.1
print(f"El preu és {preu}€")

#Exerici 4
edat = int(input("Digues la teva edat: "))
ingressosf = int(input("Digues els teus ingresos familiars: "))
germans = int(input("Digues el numero de germans: "))
formula_beca = (germans * 5700) + 500
if ingressosf < formula_beca or germans > 4:
    beca = 4000 * ((formula_beca - ingressosf)/formula_beca)
    if edat < 18:
        beca = beca + beca * 0.1
    if germans > 4:
        beca = beca + 150
else:
    beca = 0
print(f"La beca és de {beca:.2f}€")
