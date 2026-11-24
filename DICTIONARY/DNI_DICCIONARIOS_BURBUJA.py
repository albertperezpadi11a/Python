lettersDni = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C',
              'K', 'E')
user1 = {"nombre": "Pedro Javier Morales", "direccion": "Flores 36 8º 2ª", "tfn": ["+0034345345345"],
         "compras": [1234, 423, 23]}
user2 = {"nombre": "Maite Lopez Miravet", "direccion": "Balmes 31 1º 2ª", "tfn": ["+0034234234235", "+0034239999235"],
         "compras": [12344]}
user3 = {"nombre": "Marta Garcia Suarez", "direccion": "Valencia 21 3º 1ª", "tfn": ["+0075766576575"],
         "compras": [34, 423, 23, 6]}
users = {"47474747X": user1, "24536425T": user2, "76767676H": user3}
menu_list = "*" * 90 + "\n{:10}{:25}{:25}{:15}{:>15}\n".format("DNI", "Nombre", "Direccion", "Tfn",
                                                               "Total Compras") + "*" * 90 + "\n"
menu_00 = "Welcome to the User Management Program".center(50,
                                                          "*") + "\n1)Create User\n2)Modify User\n3)Show Users\n4)Find Users\n5)List Users\n6)Exit"
menu_02X = "1)Edit Address\n2)Add Tfn\n3)Del Tfn\n4)Go Back"
menu_04 = "1)Find Users by DNI\n2)Find USers by Name\n3)Go Back"
menu_05 = "1)List Users by DNI\n2)List Users by Name\n3)List Users by Address\n4)List Users by Total Purchase\n5)Go Back"
close = False
flag_00 = True
flag_02 = False
flag_02X = False
flag_02X3 = False
flag_04 = False
flag_05 = False
while not close:
    while flag_00:
        print(menu_00)
        opt = input("Option: ")
        if not opt.isdigit() or int(opt) not in range(1, 7):
            print("Invalid Option")
            input("Press any key to continue")
        else:
            opt = int(opt)
            if opt == 1:
                dni = input("DNI: ")
                if not dni.isdigit():
                    print("Invalid Option")
                    input("Press any key to continue")
                else:
                    dni = dni + lettersDni[int(dni) % 23]
                    name = input("Name: ")
                    address = input("Address: ")
                    num_tfns = input("Number of tfn: ")
                    if not num_tfns.isdigit():
                        print("Invalid Option")
                        input("Press any key to continue")
                    else:
                        num_tfns = int(num_tfns)
                        tfns = []
                        for i in range(num_tfns):
                            tfn = input("Tfn{}: ".format(i + 1))
                            tfns.append(tfn)
                        num_buy = input("Number of buy orders: ")
                        if not num_buy.isdigit():
                            print("Invalid Option")
                            input("Press any key to continue")
                        else:
                            num_buy = int(num_buy)
                            buy_list = []
                            for i in range(num_buy):
                                buy = input("Buy Order Price: ")
                                while not buy.isdigit():
                                    print("Insert a valid number")
                                buy = int(buy)
                                buy_list.append(buy)
                            users[dni] = {"nombre": name, "direccion": address, "tfn": tfns, "compras": buy_list}
            elif opt == 2:
                flag_00 = False
                flag_02 = True
            elif opt == 3:
                users_dni = list(users.keys())
                data = ""
                for dni in users_dni:
                    totalb = 0
                    name = users[dni]["nombre"]
                    address = users[dni]["direccion"]
                    buy_list = users[dni]["compras"]
                    for buy in buy_list:
                        totalb = totalb + buy
                    tfns = users[dni]["tfn"]
                    for i in range(len(tfns)):
                        if i == 0:
                            data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                        else:
                            data = data + "{:60}{:15}\n".format("", tfns[i])
                    data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")
            elif opt == 4:
                flag_00 = False
                flag_04 = True
            elif opt == 5:
                flag_00 = False
                flag_05 = True
            else:
                flag_00 = False
                close = True
    while flag_02:
        data = ""
        users_dni = list(users.keys())
        for i in range(len(users_dni)):
            data = data + "{}){} - {}\n".format(i + 1, users_dni[i], users[users_dni[i]]["nombre"])
            if i == len(users_dni) - 1:
                data = data + "{})Go Back".format(i + 2)
        print(data)
        opt = input("Option: ")
        if not opt.isdigit() or int(opt) not in range(1, len(users_dni) + 2):
            print("Invalid Option")
            input("Press any key to continue")
        else:
            opt = int(opt)
            if opt in range(1, len(users_dni) + 1):
                dni = users_dni[opt - 1]
                flag_02 = False
                flag_02X = True
            else:
                flag_02 = False
                flag_00 = True
    while flag_02X:
        print("Editing {} - {}".format(dni, users[dni]["nombre"]))
        print(menu_02X)
        opt = input("Option: ")
        if not opt.isdigit() or int(opt) not in range(1, 5):
            print("Invalid Option")
            input("Press any key to continue")
        else:
            opt = int(opt)
            if opt == 1:
                print("Current Address: {}".format(users[dni]["direccion"]))
                address = input("New Address: ")
                users[dni]["direccion"] = address
            elif opt == 2:
                tfn = input("New Tfn: ")
                users[dni]["tfn"].append(tfn)
            elif opt == 3:
                flag_02X = False
                flag_02X3 = True
            else:
                flag_02X = False
                flag_02 = True
    while flag_02X3:
        data = ""
        for i in range(len(users[dni]["tfn"])):
            data = data + "{}){}\n".format(i + 1, users[dni]["tfn"][i])
        data = data + "{})Go Back".format(len(users[dni]["tfn"]) + 1)
        print("Deleting Tfn\n" + data)
        opt = input("Option: ")
        if not opt.isdigit() or int(opt) not in range(1, len(users[dni]["tfn"]) + 2):
            print("Invalid Option")
            input("Press any key to continue")
        else:
            opt = int(opt)
            if opt == len(users[dni]["tfn"]) + 1:
                flag_02X3 = False
                flag_02X = True
            else:
                users[dni]["tfn"].remove(users[dni]["tfn"][opt - 1])
    while flag_04:
        print(menu_04)
        opt = input("Option: ")
        if not opt.isdigit() or int(opt) not in range(1, 7):
            print("Invalid Option")
            input("Press any key to continue")
        else:
            opt = int(opt)
            if opt == 1:
                dni_ts = input("DNI to search: ")
                users_dni = list(users.keys())
                data = ""
                for dni in users_dni:
                    if dni_ts in dni:
                        totalb = 0
                        name = users[dni]["nombre"]
                        address = users[dni]["direccion"]
                        buy_list = users[dni]["compras"]
                        for buy in buy_list:
                            totalb = totalb + buy
                        tfns = users[dni]["tfn"]
                        for i in range(len(tfns)):
                            if i == 0:
                                data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                            else:
                                data = data + "{:60}{:15}\n".format("", tfns[i])
                        data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")
            elif opt == 2:
                name_ts = input("Name to search: ")
                users_dni = list(users.keys())
                data = ""
                for dni in users_dni:
                    if name_ts in users[dni]["nombre"]:
                        totalb = 0
                        name = users[dni]["nombre"]
                        address = users[dni]["direccion"]
                        buy_list = users[dni]["compras"]
                        for buy in buy_list:
                            totalb = totalb + buy
                        tfns = users[dni]["tfn"]
                        for i in range(len(tfns)):
                            if i == 0:
                                data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                            else:
                                data = data + "{:60}{:15}\n".format("", tfns[i])
                        data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")
            else:
                flag_04 = False
                flag_05 = True
    while flag_05:
        print(menu_05)
        opt = input("Option: ")
        if not opt.isdigit() or int(opt) not in range(1, 7):
            print("Invalid Option")
            input("Press any key to continue")
        else:
            opt = int(opt)
            if opt == 1:
                users_dni = list(users.keys())
                for j in range(len(users_dni) - 1):
                    for i in range(len(users_dni) - 1 - j):
                        if users_dni[i] > users_dni[i + 1]:
                            aux = users_dni[i]
                            users_dni[i] = users_dni[i + 1]
                            users_dni[i + 1] = aux
                data = ""
                for dni in users_dni:
                    totalb = 0
                    name = users[dni]["nombre"]
                    address = users[dni]["direccion"]
                    buy_list = users[dni]["compras"]
                    for buy in buy_list:
                        totalb = totalb + buy
                    tfns = users[dni]["tfn"]
                    for i in range(len(tfns)):
                        if i == 0:
                            data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                        else:
                            data = data + "{:60}{:15}\n".format("", tfns[i])
                    data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")

            elif opt == 2:
                users_dni = list(users.keys())
                for j in range(len(users_dni) - 1):
                    for i in range(len(users_dni) - 1 - j):
                        if users[users_dni[i]]["nombre"] > users[users_dni[i + 1]]["nombre"]:
                            aux = users_dni[i]
                            users_dni[i] = users_dni[i + 1]
                            users_dni[i + 1] = aux
                data = ""
                for dni in users_dni:
                    totalb = 0
                    name = users[dni]["nombre"]
                    address = users[dni]["direccion"]
                    buy_list = users[dni]["compras"]
                    for buy in buy_list:
                        totalb = totalb + buy
                    tfns = users[dni]["tfn"]
                    for i in range(len(tfns)):
                        if i == 0:
                            data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                        else:
                            data = data + "{:60}{:15}\n".format("", tfns[i])
                    data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")

            elif opt == 3:
                users_dni = list(users.keys())
                for j in range(len(users_dni) - 1):
                    for i in range(len(users_dni) - 1 - j):
                        if users[users_dni[i]]["direccion"] > users[users_dni[i + 1]]["direccion"]:
                            aux = users_dni[i]
                            users_dni[i] = users_dni[i + 1]
                            users_dni[i + 1] = aux
                data = ""
                for dni in users_dni:
                    totalb = 0
                    name = users[dni]["nombre"]
                    address = users[dni]["direccion"]
                    buy_list = users[dni]["compras"]
                    for buy in buy_list:
                        totalb = totalb + buy
                    tfns = users[dni]["tfn"]
                    for i in range(len(tfns)):
                        if i == 0:
                            data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                        else:
                            data = data + "{:60}{:15}\n".format("", tfns[i])
                    data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")

            elif opt == 4:
                users_dni = list(users.keys())
                total_buy = {}
                for dni in users:
                    total_buy[dni] = 0
                    for buy in users[dni]["compras"]:
                        total_buy[dni] = total_buy[dni] + buy
                for j in range(len(users_dni) - 1):
                    for i in range(len(users_dni) - 1 - j):
                        # buy_list = users[users_dni[i]]["compras"]
                        # totalb = 0
                        # totalb2 = 0
                        # for buy in buy_list:
                        #     totalb = totalb + buy
                        # buy_list2 = users[users_dni[i + 1]]["compras"]
                        # for buy in buy_list2:
                        #     totalb2 = totalb2 + buy
                        if total_buy[users_dni[i]] < total_buy[users_dni[i + 1]]:
                            aux = users_dni[i]
                            users_dni[i] = users_dni[i + 1]
                            users_dni[i + 1] = aux
                data = ""
                for dni in users_dni:
                    totalb = 0
                    name = users[dni]["nombre"]
                    address = users[dni]["direccion"]
                    buy_list = users[dni]["compras"]
                    for buy in buy_list:
                        totalb = totalb + buy
                    tfns = users[dni]["tfn"]
                    for i in range(len(tfns)):
                        if i == 0:
                            data = data + "{:10}{:25}{:25}{:15}{:>15}\n".format(dni, name, address, tfns[i], totalb)
                        else:
                            data = data + "{:60}{:15}\n".format("", tfns[i])
                    data = data + "-" * 90 + "\n"
                print(menu_list + data)
                input("Press any key to continue")

            else:
                flag_05 = False
                flag_00 = True
