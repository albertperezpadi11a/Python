# En un organisme tenim bacteris B1, B2 i cèl·lules CA
B1 = 100
B2 = 50
CA = 100
seconds = 0
while (B1 > 0 and CA > 0) or (B2 > 0 and CA > 0) or (B1 > 0 and B2 > 0):
    # Cada segundo
    if seconds != 0:
        #   * las celulas CA, se duplican
        CA = CA * 2

    # Cada 2 segundos
    if seconds % 2 == 0 and seconds != 0:
        #   * cada bacteria B1 se come 3 celulas CA y se dublica, en caso de no
        #     tener suficientes celulas para comer, se muere.
        if CA >= B1 * 3:
            CA = CA - B1 * 3
            B1 = B1 * 2
        else:
            B1 = CA // 3 * 2
            CA = CA % 3

    # Cada 3 segundos
    if seconds % 3 == 0 and seconds != 0:
        #   * cada 2 bacterias B2 matan 1 bacteria B1
        if B1 > B2 // 2:
            B1 = B1 - B2 // 2
        else:
            B1 = 0
        #   * cada bacteria B1 se come 2 celulas CA y se duplica, en caso de no
        #     tener suficientes celulas para comer, se muere.
        if CA >= B1 * 2:
            CA = CA - B1 * 2
            B1 = B1 * 2
        else:
            B1 = CA // 2 * 2
            CA = CA % 2

    # Cada 4 segundos
    if seconds % 4 == 0 and seconds != 0:
        #   * cada 5 celulas CA, matan una Bacteria B1
        if B1 > CA // 5:
            B1 = B1 - CA // 5
        else:
            B1 = 0
        #   * cada 3 Bacterias B1 matan una B2
        if B2 > B1 // 3:
            B2 = B2 - B1 // 3
        else:
            B2 = 0

    print("Segundo: {}, B1: {}, B2: {}, CA: {}".format(seconds, B1, B2, CA))
    seconds = seconds + 1

