#Capçalera
capçalera = "Magatzem Logistic".center(50,"*") + "\n" + \
    "{:20}{:>10}{:>10}{:>10}\n".format("Producte","Quantitat","Preu","Total") + \
    "*" * 50 + "\n"
productes = ""
total = 0

#Primer Producte
nom = input("Primer Producte: ")
quantitat = int(input("Quantitat: "))
preu = float(input("Preu: "))
productes = productes + "{:20}{:10}{:10.3f}{:10.2f}\n".format(nom,quantitat,preu,quantitat*preu)
total = total + quantitat*preu

#Segon Producte
nom = input("Segon Producte: ")
quantitat = int(input("Quantitat: "))
preu = float(input("Preu: "))
productes = productes + "{:20}{:10}{:10.3f}{:10.2f}\n".format(nom,quantitat,preu,quantitat*preu)
total = total + quantitat*preu

#Tercer Producte
nom = input("Tercer Producte: ")
quantitat = int(input("Quantitat: "))
preu = float(input("Preu: "))
productes = productes + "{:20}{:10}{:10.3f}{:10.2f}\n".format(nom,quantitat,preu,quantitat*preu)
total = total + quantitat*preu

#Peu de pagina
peup = "*" * 50 + "\n" + "{:>50}".format("Total Inventari") + "\n" + "{:50.2f}".format(total)
print(capçalera + productes + peup)