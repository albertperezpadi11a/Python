# Crearem la següent aplicació que simularà un joc de daus.
# Començarem amb el següent menú:
#
# ============The Best Game In The World============
# 1)New Game
# 2)New Player
# 3)Show Ranking
# 4)Exit
#
# option:
#
# Es comprovarà que lopció introduïda per lusuari és correcta. En cas d'introduir un caràcter se'ns informarà que allò que s'ha introduït no és un caràcter numèric i es tornarà a mostrar al menú.
# En cas d'introduir una opció no vàlida, se'ns mostrarà un missatge informatiu conforme l'opció no és vàlida i es tornarà a mostrar al menú.
#
# Per jugar haurem de seleccionar l'opció 1 new game. Però abans haurem d'haver introduït
# un nom de jugador que seria lopció dos new player, En cas de no haver introduït un nom de jugador, se'ns mostrarà un missatge informatiu i es tornarà a mostrar el menú.
#
# El joc o sigui l'opció 1 new game serà un joc de daus on juga el jugador contra la màquina. El joc consisteix en el següent: Cada jugador llença quatre daus, si es treu quatre daus iguals
# el jugador sumarà a quinze punts i tornarà a tirar de nou- En cas de treure un trio, el jugador sumarà vuit punts i tornarà a tirar. En cas de treure una parella el jugador sumarà dos punts,
# una parella i dues parelles puntuen el mateix. Guanya el jugador que arribi a cinquanta punts.
# Si guanya el jugador, s'afegirà al ranking
import random

menu = "The Best Game In The World".center(50,"=") + "\n1)New Game\n2)New Player\n3)Show Ranking\n4)Exit\n"
ranking = "Ranking".center(30,"=") + "\n" + "{:15}{:>15}\n".format("Name","Points")
player = ""

close = False
nameset = False

while not close:
    print(menu)
    opt = input("Option: ")
    if not opt.isdigit():
        print("Option has to be numeric")
        input("Press Enter to continue...\n")
    elif int(opt) not in range(1, 5):
        print("Option out of range")
        input("Press Enter to continue...\n")
    else:
        opt = int(opt)
        if opt == 1 and not nameset:
            print("Player Name not set")
            input("Press Enter to continue...\n")
        elif opt == 1 and nameset:
            pcpoints = 0
            ppoints = 0
            while ppoints < 50 and pcpoints < 50:
                roundpc = 0
                roundp = 0
                #Punts Jugador
                pdice1 = random.randint(1,6)
                pdice2 = random.randint(1,6)
                pdice3 = random.randint(1,6)
                pdice4 = random.randint(1,6)
                if pdice1 == pdice2 == pdice3 == pdice4:
                    ppoints = ppoints + 15
                    roundp = 15
                elif pdice1 == pdice2 == pdice3 or pdice2 == pdice3 == pdice4 or pdice1 == pdice3 == pdice4 or pdice1 == pdice2 == pdice4:
                    ppoints = ppoints + 8
                    roundp = 8
                elif pdice1 == pdice2 or pdice2 == pdice3 or pdice1 == pdice4 or pdice3 == pdice4 or pdice1 == pdice3 or pdice2 == pdice4:
                    ppoints = ppoints + 2
                    roundp = 2

                #Punts ordinador
                pcdice1 = random.randint(1,6)
                pcdice2 = random.randint(1,6)
                pcdice3 = random.randint(1,6)
                pcdice4 = random.randint(1,6)
                if pcdice1 == pcdice2 == pcdice3 == pcdice4:
                    pcpoints = pcpoints + 15
                    roundpc = 15
                elif pcdice1 == pcdice2 == pcdice3 or pcdice2 == pcdice3 == pcdice4 or pcdice1 == pcdice3 == pcdice4 or pcdice1 == pcdice2 == pcdice4:
                    pcpoints = pcpoints + 8
                    roundpc = 8
                elif pcdice1 == pcdice2 or pcdice2 == pcdice3 or pcdice1 == pcdice4 or pcdice3 == pcdice4 or pcdice1 == pcdice3 or pcdice2 == pcdice4:
                    pcpoints = pcpoints + 2
                    roundpc = 2

                #Missatge
                print("{}'s Dice{:5}{:5}{:5}{:5}".format(player,pdice1,pdice2,pdice3,pdice4))
                print("PC's Dice{:5}{:5}{:5}{:5}".format(pcdice1,pcdice2,pcdice3,pcdice4))
                print("{}'s Points: round = {}, total = {}".format(player,roundp,ppoints))
                print("PC's Points: round = {}, total = {}".format(roundpc,pcpoints))
                roundpc =  0
                roundp = 0
                if ppoints >= 50 and not pcpoints >= 50:
                    ranking = ranking + "{:15}{:15}\n".format(player,ppoints)
                    print("You WIN!")
                elif pcpoints >= 50:
                    print("You LOSE!")
        elif opt == 2:
            player = input("Player Name: ")
            nameset = True
        elif opt == 3:
            print(ranking)
            input("Press Enter to continue...\n")
        else:
            close = True