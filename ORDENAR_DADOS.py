

Da1 = int(input("Dime un dado: "))
Da2 = int(input("Dime un dado: "))
Da3 = int(input("Dime un dado: "))
Dd1 = int(input("Dime un dado: "))
Dd2 = int(input("Dime un dado: "))
Dd3 = int(input("Dime un dado: "))

#Ordenar ataque
if Da1 < Da2:
    aux = Da1
    Da1 = Da2
    Da2 = aux
if Da2 < Da3:
    aux = Da3
    Da3 = Da2
    Da2 = aux
if Da1 < Da2:
    aux = Da1
    Da1 = Da2
    Da2 = aux

#Ordenar defensa
if Dd1 < Dd2:
    aux = Dd1
    Dd1 = Dd2
    Dd2 = aux
if Dd2 < Dd3:
    aux = Dd2
    Dd2 = Dd3
    Dd3 = aux
if Dd1 < Dd2:
    aux = Dd1
    Dd1 = Dd2
    Dd2 = aux
print(f"{Da1} {Da2} {Da3}")