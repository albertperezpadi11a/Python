import random
from random import choice

# Exercici1
num = random.randint(1,10)
print(num)
unum = int(input("Guess the number between 1 and 10: "))
while unum != num:
    print("Wrong number! Try again...")
    unum = int(input("Guess the number: "))
else:
    print("Correct!")

# Exercici2
num = random.randint(1,100)
print(num)
unum = int(input("Guess the number between 1 and 100: "))
tries = 5
while unum != num and not tries == 0:
    if unum < num and tries - 1 != 0:
        tries = tries - 1
        print("Number is bigger. {} tries left".format(tries))
        unum = int(input("Guess the number between 1 and 100: "))
    elif unum > num and tries - 1 != 0:
        tries = tries - 1
        print("Number is smaller. {} tries left".format(tries))
        unum = int(input("Guess the number between 1 and 100: "))
    else:
        tries = 0
        print("No tries left!")
if tries != 0:
    print("Correct!")

# Exercici3
winner = False
while not winner:
    num = random.randint(1,3)
    if num == 1:
        pc = "rock"
    elif num == 2:
        pc = "paper"
    else:
        pc = "scissors"
    unum = int(input("Choose Rock, Paper, or Scissors (1-3): "))
    if unum == 1:
        user = "rock"
    elif unum == 2:
        user = "paper"
    else:
        user = "scissors"
    if num == unum:
        print("Draw! Both players chose {}".format(user))
    elif (unum == 1 and num == 3) or (unum == 2 and num == 1) or (unum == 3 and num == 2):
        print("PC chose {}, you chose {}.\nYou win!".format(pc, user))
        winner = True
    else:
        print("PC chose {}, you chose {}.\nYou lost!".format(pc, user))
        winner = True

# Exercici4
a = 0
b = 0
winned = 0
losed = 0
close = False
while not close:
    while a == b:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    opt = input("Apostes per A o per B?: ")
    if a > b and opt == "A":
        print("A treu un {} i B treu un {}  HAS GUANYAT!".format(a,b))
        winned = winned + 1
    elif a < b and opt == "B":
        print("A treu un {} i B treu un {}  HAS GUANYAT!".format(a,b))
        winned = winned + 1
    else:
        print("A treu un {} i B treu un {}  HAS PERDUT!".format(a,b))
        losed = losed + 1
    print("Portes {} partides guanyades i {} partides perdudes".format(winned, losed))
    try_again = input("Vols provar un altre cop? (S/N): ")
    if try_again == "N":
        close = True
    else:
        a = 0
        b = 0