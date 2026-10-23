menu_00 = "Contacts".center(30,"*") + "\n1)Show Contatcs\n2)New Contact\n3)Edit Contact\n" + \
                                             "4)Delete Contact\n5)Search Contact\n6)Exit"
menu_01 = "Contacts List".center(60,"*") + "\n" + "{:25}{:25}{:>10}".format("Name", "Address", "P.Number") + "\n" + "*" * 60
menu_03 = "Edit Contact".center(62,"*")
menu_031 = "Editing Contact".center(30,"*") + "\n1)Edit Adrress\n2)Add Phone Number\n3)Delete Phone Number\n4)Go Back"
menu_05 = "Search Contact".center(60,"*")
close = False
flag_00 = True
flag_03 = False
flag_031 = False
flag_0313 = False
flag_04 = False
flag_05 = False
contacts = "Albert Pérez Padilla*Jacint Verdaguer 7*682548566#45#67#69#420#;A*A*A#;B*B*B#;"
contact = ""
while not close:
    while flag_00:
        print(menu_00)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range (1,7):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == 1:
                print(menu_01)
                start = 0
                end = 0
                for i in range(contacts.count(";")):
                    if i == 0:
                        start = 0
                        end = contacts.find(";")
                    else:
                        start = end + 1
                        end = contacts.find(";", start)
                    contact = contacts[start:end]
                    first_spacing = contact.find("*")
                    second_spacing = contact.find("*", first_spacing + 1)
                    name = contact[:first_spacing]
                    address = contact[first_spacing + 1:second_spacing]
                    number = contact[second_spacing + 1:end]
                    print("{:25}{:25}{:>10}".format(name, address, number))
                input("Press Enter to continue...")
            elif opt == 2:
                print("Adding New Contact")
                name = input("Name: ")
                address = input("Address: ")
                number_count = input("Number of Phone Numbers to add: ")
                while not number_count.isdigit():
                    print("Enter a decimal number")
                    number_count = input("Number of Phone Numbers to add: ")
                else:
                    number_count = int(number_count)
                    for i in range(1,number_count):
                        phone = input("Phone Number{}: ".format(i))
                        contacts = contacts + name + "*" + address + "*" + phone + ";"
            elif opt == 3:
                flag_00 = False
                flag_03 = True
            elif opt == 4:
                flag_00 = False
                flag_04 = True
            elif opt == 5:
                flag_00 = False
                flag_05 = True
            else:
                flag_00 = False
                close = True
    while flag_03:
        print(menu_03)
        start = 0
        end = 0
        for i in range(contacts.count(";")):
            if i == 0:
                start = 0
                end = contacts.find(";")
            else:
                start = end + 1
                end = contacts.find(";", start)
            contact = contacts[start:end]
            first_spacing = contact.find("*")
            second_spacing = contact.find("*", first_spacing + 1)
            name = contact[:first_spacing]
            address = contact[first_spacing + 1:second_spacing]
            number = contact[second_spacing + 1:end-1]
            print("{}){:25}{:25}{:>10}".format(i + 1, name, address, number))
        print("{})Go Back".format(contacts.count(";")+1))
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range (1,contacts.count(";") + 2):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == contacts.count(";") + 1:
                flag_03 = False
                flag_00 = True
            else:
                start_contact = 0
                end_contact = 0
                for j in range(opt):
                    if j == 0:
                        start_contact = 0
                        end_contact = contacts.find(";")
                    else:
                        start_contact = end_contact + 1
                        end_contact = contacts.find(";", start_contact)
                    contact = contacts[start_contact:end_contact + 1]
                    flag_03 = False
                    flag_031 = True
    while flag_031:
        print(menu_031)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range (1,5):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == 1:
                start = contact.find("*") + 1
                end = contact.find("*", start)
                print("Current Address: {}".format(contact[start:end]))
                address = input("New addres: ")
                contact = contact[:start] + address + contact[end:]
            elif opt == 2:
                final = contact.find(";")
                number = input("New Phone Number: ")
                contact = contact[:final] + "#" + number + contact[final:]
            elif opt == 3:
                flag_031 = False
                flag_0313 = True
            else:
                flag_031 = False
                flag_03 = True
    while flag_0313:
        menu_0313 = "Deleting Number".center(30, "*") + "\n"
        for i in range(contact.count("#")):
            if i == 0:
                start = contact.find("*", contact.find("*") + 1) + 1
                end = contact.find("#", start)
            else:
                start = contact.find("#", end) + 1
                end = contact.find("#", start + 1)
            number = contact[start:end]
            menu_0313 = menu_0313 + "{}){}\n".format(i + 1,number)
        menu_0313 = menu_0313 + "{})Go Back".format(contact.count("#") + 1)
        print(menu_0313)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is out of range")
            input("Press Enter to continue...")
        elif not int(opt) in range(1,contact.count("#") + 2):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == contact.count("#") + 1:
                flag_0313 = False
                flag_031 = True
            else:
                print(contact)
                start = 0
                end = 0
                for j in range(opt):
                    if j == 0:
                        start = contact.find("*", contact.find("*") + 1) + 1
                        end = contact.find("#", start) + 1
                        if end == 0:
                            end = contact.find(";")
                    else:
                        start = contact.find("#", end - 1)
                        end = contact.find("#", start + 1)
                contact = contact[:start] + contact[end:]
                print(contact)
                end_contact = contacts.find(";", start_contact)
                contacts = contacts[:start_contact] + contact + contacts[end_contact + 1:]
                print(contacts)
    while flag_04:
        menu04 = "Delete Contact".center(60,"*") + "\n"
        for i in range(contacts.count(";")):
            if i == 0:
                start = 0
                end = contacts.find(";")
            else:
                start = end + 1
                end = contacts.find(";", start)
            contact = contacts[start:end]
            first_spacing = contact.find("*")
            second_spacing = contact.find("*", first_spacing + 1)
            name = contact[:first_spacing]
            address = contact[first_spacing + 1:second_spacing]
            menu04 = menu04 + str(i + 1) + ")" + "{:20}{:20}\n".format(name, address)
        menu04 = menu04 + str(contacts.count(";") + 1) + ")Go Back"
        print(menu04)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif not int(opc)  in range(1,contacts.count(";")+2):
            print("Option Out Of Range")
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc == contacts.count(";")+1:
                flag_00 = True
                flag_04 = False
            else:
                start = 0
                end = 0
                for j in range(opc):
                    if j == 0:
                        start = 0
                        end = contacts.find(";")
                    else:
                        start = end + 1
                        end = contacts.find(";", start)
                    contact = contacts[start:end]
                #print(contact)
                contacts = contacts[:start] + contacts[end + 1:]
    while flag_05:
        print(menu_05)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range (contacts.count(";")):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)