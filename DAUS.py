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
menu = "The Best Game In The World".center(50,"*") + "\n1)New Game\n2)New Player\n3)Show Ranking\4)Exit"
close = False
while not close:
    opt = input("Option: ")
    while not opt.isdigit() or  < opt: