import  random
# Exercici 1
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("El dau 1 ha sortit {} i el dau 2 {}".format(dice1, dice2))
# Exercici 2
sequence = ""
for i in range(2,101,2):
    print(i, end=" ")
# Exercici 3
num = int(input("\nDigues un número: "))
for i in range(2,num + 1,2):
    print(i, end=" ")
