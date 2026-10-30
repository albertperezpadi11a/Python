menu_00 = "Contacts".center(30, "*") + "\n1)Show Contatcs\n2)New Contact\n3)Edit Contact\n" + \
          "4)Delete Contact\n5)Search Contact\n6)Exit"
menu_031 = "Editing Contact".center(30, "*") + "\n1)Edit Adrress\n2)Add Phone Number\n3)Delete Phone Number\n4)Go Back"
menu_05 = "Search Contact".center(30, "*") + "\n1)Search by Name\n2)Search by Address\n3)Search by Number\n4)Go Back"
close = False
flag_00 = True
flag_03 = False
flag_031 = False
flag_0311 = False
flag_04 = False
flag_05 = False
contacts = [
    ["Alberto Castaño Sanchez", "Balmes 27 1º2º", ["666344551", "777000000"]],
    ["Enrique Casado Ruiz", "Rocafort 234 5º1º", ["674343536", "937182323", "345343434"]],
    ["Esther Flores Ruiz", "Numancia 345 10º A", ["657876543"]],
    ["Maria Lopez Vallejo", "Bonavista 43 3º3º", ["667344556", "937249898"]]
]
while not close:
    while flag_00:
        print(menu_00)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range(1, 7):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == 1:
                menu_01 = "Contact List".center(70, "=") + "\n" + "{:30}{:20}{:>20}\n".format("Name", "Address", "Tfn") + "=" * 70 + "\n"
                for i in range(len(contacts)):
                    contact = contacts[i]
                    name = contact[0]
                    address = contact[1]
                    tfns = contact[2]
                    for j in range(len(tfns)):
                        tfn = tfns[j]
                        if j == 0:
                            menu_01 = menu_01 + ("{:30}{:20}{:>20}\n".format(name, address, tfn))
                        else:
                            menu_01 = menu_01 + "{:>70}\n".format(tfn)
                    if i != len(contacts) - 1:
                        menu_01 = menu_01 + "-" * 70 + "\n"
                print(menu_01)
                input("Press Enter to continue...")
            elif opt == 2:
                print("Adding New Contact")
                name = input("Name: ")
                address = input("Address: ")
                tfns_count = input("Number of Phone Numbers to add: ")
                while not tfns_count.isdigit():
                    print("Enter a decimal number")
                    tfns_count = input("Number of Phone Numbers to add: ")
                else:
                    tfns = []
                    tfns_count = int(tfns_count)
                    for i in range(1, tfns_count + 1):
                        phone = input("Phone Number {}: ".format(i))
                        tfns.append(phone)
                    contact = [name,address,tfns]
                    for i in range(len(contacts)):
                        if not contact in contacts:
                            if name < contacts[i][0]:
                                contacts.insert(i, contact)
                            elif i == len(contacts) - 1:
                                contacts.append(contact)
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
        menu_03 = "Edit Contact".center(62, "*") + "\n"
        for i in range(len(contacts)):
            menu_04 = menu_03 + "{}){}; {}\n".format(i + 1, contacts[i][0], contacts[i][1])
        menu_03 = menu_03 + "{})Go Back".format(len(contacts) + 1)
        print(menu_03)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range(1, len(contacts) + 2):
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
        elif not int(opt) in range(1, 5):
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
                contacts = contacts[:start_contact] + contact[:-1] + contacts[end_contact:]
            elif opt == 2:
                final = contact.find(";")
                number = input("New Phone Number: ")
                contact = contact[:final] + number + "#" + contact[final:]
                contacts = contacts[:start_contact] + contact[:-1] + contacts[end_contact:]
            elif opt == 3:
                flag_031 = False
                flag_0311 = True
            else:
                flag_031 = False
                flag_03 = True
    while flag_0311:
        menu_0313 = "Deleting Number".center(30, "*") + "\n"
        start = 0
        end = 0
        for i in range(contact.count("#")):
            if i == 0:
                start = contact.find("*", contact.find("*") + 1) + 1
                end = contact.find("#", start)
            else:
                start = contact.find("#", end) + 1
                end = contact.find("#", start + 1)
            number = contact[start:end]
            menu_0313 = menu_0313 + "{}){}\n".format(i + 1, number)
        menu_0313 = menu_0313 + "{})Go Back".format(contact.count("#") + 1)
        print(menu_0313)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is out of range")
            input("Press Enter to continue...")
        elif not int(opt) in range(1, contact.count("#") + 2):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == contact.count("#") + 1:
                flag_0311 = False
                flag_031 = True
            else:
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
                end_contact = contacts.find(";", start_contact)
                contacts = contacts[:start_contact] + contact + contacts[end_contact + 1:]
                print("Number succesfully deleted")
    while flag_04:
        menu_04 = "Delete Contact".center(60, "*") + "\n"
        for i in range(len(contacts)):
            menu_04 = menu_04 + "{}){}; {}\n".format(i + 1, contacts[i][0], contacts[i][1])
        menu_04 = menu_04 + "{})Go Back".format(len(contacts) + 1)
        print(menu_04)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Non-Numeric Option ")
            input("Enter to continue")
        elif not int(opc) in range(1,len(contacts) + 2):
            print("Option Out Of Range")
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc == len(contacts) + 1:
                flag_04 = False
                flag_00 = True
            else:
                contacts.remove(contacts[opc - 1])
                #contacts.pop(opc - 1)
                #contacts = contacts[:opc - 1] + contacts[opc:]
    while flag_05:
        print(menu_05)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range(1, 5):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            #Pa que Pycharm no me llore
            search_name = ""
            search_address = ""
            to_search = ""
            search_number = ""
            # hasta qui
            sname = False
            if opt == 4:
                flag_05 = False
                flag_00 = True
            elif opt == 1:
                search_name = input("Enter Name to search: ")
                sname = True
            elif opt == 2:
                search_address = input("Enter Address to search: ")
            elif opt == 3:
                search_number = input("Enter Number to search: ")
            if sname:
                to_search = search_name.lower()
            else:
                to_search = search_address.lower()
            menu_051 = "Contact List".center(70, "=") + "\n" + "{:30}{:20}{:>20}\n".format("Name", "Address", "Tfn") + "=" * 70 + "\n"
            if len(to_search) > 0:
                for i in range(len(contacts)):
                    contact = contacts[i]
                    if (to_search in contact[0].lower() and sname) or (to_search in contact[1].lower() and not sname):
                        tfns = contact[2]
                        for j in range(len(tfns)):
                            tfn = tfns[j]
                            if j == 0:
                                menu_051 = menu_051 + ("{:30}{:20}{:>20}\n".format(contact[0], contact[1], tfn))
                            else:
                                menu_051 = menu_051 + "{:>70}\n".format(tfn)
                        if i != len(contacts) - 1:
                            menu_051 = menu_051 + "-" * 70 + "\n"
                print(menu_051)
                input("Press Enter to continue...")
            else:
                for i in range(len(contacts)):
                    contact = contacts[i]
                    tfns = contact[2]
                    for z in range(len(tfns)):
                        if search_number in tfns[z] and not contact[0] in menu_051:
                            for j in range(len(tfns)):
                                    tfn = tfns[j]
                                    if j == 0:
                                        menu_051 = menu_051 + ("{:30}{:20}{:>20}\n".format(contact[0], contact[1], tfn))
                                    else:
                                        menu_051 = menu_051 + "{:>70}\n".format(tfn)
                print(menu_051)
                input("Press Enter to continue...")