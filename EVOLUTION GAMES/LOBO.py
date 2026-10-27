# En un pueblo, existen tres entidades:
# Cazadores
# Lobos
# Ovejas
# Condiciones iniciales:
#       cazadores: 6
#        lobos: 8
#       ovejas: 12
hunters = 6
wolfs = 8
sheeps = 12
day = 0
while hunters != 0 and sheeps != 0 and wolfs != 0:
    # Cada dia:
    if day != 0:
        #     Cada 5 ovejas generan una nueva oveja
        sheeps = sheeps + sheeps // 5

    # Cada 2 dias:
    if day % 2 == 0 and day != 0:
        #     Cada 3 lobos  se comen  1 oveja y estos 3 lobos crean un nuevo lobo. Si algun lobo no encuentra más
        #     un grupo de 2 lobos más para cazar, muere.
        #     Lo lobos que no tengan ovejas para cazar mueren .
        if sheeps >= wolfs // 3:
            sheeps = sheeps - wolfs // 3
            wolfs = wolfs + wolfs // 3  - wolfs % 3
        else:
            wolfs = sheeps * 3 + wolfs // 3
            sheeps = 0
        #     Viene un nuevo cazador al pueblo
        hunters = hunters + 1

    # Cada 3 dias:
    if day % 3 == 0 and day != 0:
        #     Cada 2 cazadores matan un lobo.
        if wolfs >= hunters // 2:
            wolfs = wolfs - hunters // 2
        else:
            wolfs = 0
        #     Luego, cada 2 lobos sobrevivientes se come 1 oveja y de estos lobos nace un nuevo lobo. Si un
        #     lobo no encuentra otro lobo que le acompañe cazando ovejas, muere.
        #     Lo lobos que no tengan ovejas para cazar mueren .
        if sheeps >= wolfs // 2:
            sheeps = sheeps - wolfs // 2
            wolfs = wolfs + wolfs // 2 - wolfs % 2
        else:
            wolfs = sheeps * 2 + wolfs // 2
            sheeps = 0

# Cada 4 dias:
#     • Cada 30 ovejas matan un lobo.
#     • Además, cada 10 lobos matan un cazador.
    if day % 4 == 0 and day != 0:
        if wolfs >= sheeps // 30:
            wolfs = wolfs - sheeps // 30
            if hunters > wolfs // 10:
                hunters = hunters - wolfs // 10
            else:
                hunters = 0
        else:
            wolfs = 0
    print("Dia = {}, Lobos = {}, Ovejas = {}, Cazadores = {}".format(day, wolfs, sheeps, hunters))
    day = day + 1