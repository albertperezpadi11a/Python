# En un sistema automatizado tenemos robots R1, drones D2 y estaciones de energía E.
R1 = 10
D2 = 6
E = 50
dias = 0
while R1 > 0 and D2 > 0 and E > 0:
    # Cada dia:
    if dias != 0:
        #     Las estaciones de energía E se duplican.
        E = E * 2

    # Cada 2 dias:
    if dias % 2 == 0 and dias != 0:
        #     Cada robot R1 consume 4 estaciones E para recargarse y se duplica.
        #     Si no hay suficientes estaciones, el robot se apaga (muere).
        if E >= R1 * 4:
            E = E - R1 * 4
            R1 = R1 * 2
        else:
            R1 = E // 4 * 2
            E = E % 4

    # Cada 3 dias:
    if dias % 3 == 0 and dias != 0:
        #     Cada 2 drones D2 desactivan 1 robot R1.
        if R1 > D2 // 2:
            R1 = R1 - D2 // 2
        else:
            R1 = 0
        #     Luego, cada dron consume 3 estaciones E para potenciarse y se duplica.
        #       Si no hay suficientes estaciones, se apaga.
        if E >= D2 * 3:
            E = E - D2 * 3
            D2 = D2 * 2
        else:
            D2 = E // 3 * 2
            E = E % 3

    # Cada 4 dias:
    if dias % 4 == 0 and dias != 0:
        #     Cada 50 estaciones sobrecargan y destruyen 2 robots.
        if R1 > E // 50 * 2:
            R1 = R1 - E // 50 * 2
        else:
            R1 = 0
        #     Además, cada 4 robots R1 logran hackear y destruyen 1 drone .
        if D2 > R1 // 4:
            D2 = D2 - R1 // 4
        else:
            D2 = 0

    print("Dias: {}, R1: {}, D2: {}, E: {}".format(dias, R1, D2, E))
    dias = dias + 1