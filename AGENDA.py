menu_00 = "Contacts".center(30,"*") + "\n1)Show Contatcs\n2)New Contact\n3)Edit Contact\n" + \
                                             "4)Delete Contact\n5)Search Contact\n6)Exit"
menu_01 = "Contacts List".center(60,"*") + "\n" + "{:25}{:25}{:>10}".format("Name", "Address", "P.Number") + "\n" + "*" * 60
menu_03 = "Edit Contact".center(62,"*")
menu_031 = "Editing Contact".center(30,"*") + "\n1)Edit Adrress\n2)Add Phone Number\n3)Delete Phone Number\n4)Go Back"
menu_04 = "Delete Contact".center(60,"*")
menu_05 = "Search Contact".center(60,"*")
close = False
flag_00 = True
flag_03 = False
flag_031 = False
flag_0313 = True
flag_04 = False
flag_05 = False
contacts = "Albert Pérez Padilla*Jacint Verdaguer 7*682548566#45#67#69#420;A*A*A;"
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
            number = contact[second_spacing + 1:end]
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
        elif not int(opt) in range (1,6):
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
                print(contact)
            elif opt == 2:
                final = contact.find(";")
                number = input("New Phone Number: ")
                contact = contact[:final] + "#" + number + contact[final:]
                print(contact)
            elif opt == 3:
                flag_031 = False
                flag_0313 = True
                menu_temp = ""
                start = 0
                end = 0
                print(contact)
                for i in range(1,contact.count("#") + 2):
                    if i == 1:
                        start = contact.find("*", contact.find("*") + 1) + 1
                        end = contact.find("#", start)
                    else:
                        start = contact.find("#", end) + 1
                        end = contact.find("#", start + 1)
                    number = contact[start:end]
                    menu_temp = menu_temp + "{}){}\n".format(i,number)
                menu_temp = menu_temp + "{})Go back".format(contact.count("#") + 2)
                flag_temp = True
                while flag_temp:
                    print(menu_temp)
                    opt = input("Option: ")
                    if not opt.isdigit():
                        print("Option is out of range")
                        input("Press Enter to continue...")
                    elif not int(opt) in range(1,contact.count("#") + 3):
                        print("Option is out of range")
                        input("Press Enter to continue...")
                    else:
                        opt = int(opt)
                        if opt == contact.count("#") + 2:
                            flag_temp = False
                        else:
                            start = 0
                            end = 0
                            for j in range(opt):
                                if j == 0:
                                    start = contact.find("*", contact.find("*") + 1) + 1
                                    end = contact.find("#", start)
                                else:
                                    start = contact.find("#", end) + 1
                                    end = contact.find("#", start + 1)
                            contact = contact[:start] + contact[end + 1:]
                            contacts = contacts[:start_contact] + contact + contacts[end_contact + 1:]
                            print(contacts)
            else:
                flag_031 = False
                flag_03 = True
    while flag_04:
        print(menu_04)
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range (contacts.count(";")):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
    while flag_05:
        opt = input("Option: ")
        if not opt.isdigit():
            print("Option is not numerical")
            input("Press Enter to continue...")
        elif not int(opt) in range (contacts.count(";")):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)