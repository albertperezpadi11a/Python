close = False
flag_000 = True
flag_001 = False
flag_002 = False
flag_011 = False
flag_012 = False
flag_021 = False
flag_022 = False

menu000 = "Menu000".center(27, "*") + "\n" + "1)Menu001\n2)Menu002\n3)Exit"
menu001 = "Menu001".center(27, "*") + "\n" + "1)Menu011\n2)Menu012\n3)Back"
menu002 = "Menu002".center(27, "*") + "\n" + "1)Menu021\n2)Menu022\n3)Back"
menu011 = "Menu011".center(27, "*") + "\n" + "1)Menu111\n2)Menu112\n3)Back"
menu012 = "Menu012".center(27, "*") + "\n" + "1)Menu121\n2)Menu122\n3)Back"
menu021 = "Menu021".center(27, "*") + "\n" + "1)Menu211\n2)Menu212\n3)Back"
menu022 = "Menu022".center(27, "*") + "\n" + "1)Menu221\n2)Menu222\n3)Back"

while not close:
    while flag_000:
        print(menu000)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu000)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                flag_000 = False
                flag_001 = True
            elif opt == 2:
                flag_000 = False
                flag_002 = True
            else:
                flag_000 = False
                close = True
    while flag_001:
        print(menu001)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu001)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                flag_001 = False
                flag_011 = True
            elif opt == 2:
                flag_001 = False
                flag_012 = True
            else:
                flag_001 = False
                flag_000 = True
    while flag_002:
        print(menu002)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu002)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                flag_002 = False
                flag_021 = True
            elif opt == 2:
                flag_002 = False
                flag_022 = True
            else:
                flag_002 = False
                flag_000 = True
    while flag_011:
        print(menu011)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu011)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                print("Selected Menu111")
            elif opt == 2:
                print("Selected Menu112")
            else:
                flag_011 = False
                flag_001 = True
    while flag_012:
        print(menu012)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu012)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                print("Selected Menu121")
            elif opt == 2:
                print("Selected Menu122")
            else:
                flag_012 = False
                flag_001 = True
    while flag_021:
        print(menu021)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu021)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                print("Selected Menu211")
            elif opt == 2:
                print("Selected Menu212")
            else:
                flag_021 = False
                flag_002 = True
    while flag_022:
        print(menu022)
        opt = input("->Option: ")
        while not opt.isdigit() or not 0 < int(opt) < 4:
            input("Incorrect value or option\nPress Enter to continue...")
            print(menu022)
            opt = input("->Option: ")
        else:
            opt = int(opt)
            if opt == 1:
                print("Selected Menu221")
            elif opt == 2:
                print("Selected Menu222")
            else:
                flag_022 = False
                flag_002 = True
