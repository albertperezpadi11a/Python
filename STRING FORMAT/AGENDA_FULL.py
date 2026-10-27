menu_00 = "Contacts".center(30,"*") + "\n1)Show Contatcs\n2)New Contact\n3)Edit Contact\n" + \
                                             "4)Delete Contact\n5)Search Contact\n6)Exit"
menu_031 = "Editing Contact".center(30,"*") + "\n1)Edit Adrress\n2)Add Phone Number\n3)Delete Phone Number\n4)Go Back"
menu_05 = "Search Contact".center(30,"*") + "\n1)Search by Name\n2)Search by Address\n3)Search by Number\n4)Go Back"
close = False
flag_00 = True
flag_03 = False
flag_031 = False
flag_0311 = False
flag_04 = False
flag_05 = False
sname = False
saddress = False
snumber = False
contacts = "Albert Perez Padilla*Jacint Verdaguer 7*682548566#67#69#420#;A*A*A#;B*B*B#;"
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
                menu_01 = "Contacts List".center(60,"*") + "\n" + "{:25}{:25}{:>10}".format("Name", "Address", "P.Number") + \
                          "\n" + "*" * 60 + "\n"
                start = 0
                end = 0
                for i in range(contacts.count(";")):
                    if i == 0:
                        start = 0
                        end = contacts.find(";") + 1
                    else:
                        start = end
                        end = contacts.find(";", start + 1) + 1
                    contact = contacts[start:end]
                    first_spacing = contact.find("*")
                    second_spacing = contact.find("*", first_spacing + 1)
                    name = contact[:first_spacing]
                    address = contact[first_spacing + 1:second_spacing]
                    if contact.count("#") > 1:
                        start_phone = 0
                        end_phone = 0
                        for j in range(contact.count("#")):
                            if j == 0:
                                start_phone = second_spacing + 1
                                end_phone = contact.find("#", start_phone)
                            else:
                                start_phone = contact.find("#", end_phone) + 1
                                end_phone = contact.find("#", start_phone + 1)
                            number = contact[start_phone:end_phone]
                            if j == 0:
                                menu_01 = menu_01 + ("{:25}{:25}{:>10}\n".format(name, address, number))
                            else:
                                menu_01 = menu_01 + ("{:>60}\n".format(number))
                    else:
                        number = contact[second_spacing + 1:contact.find("#")]
                        menu_01 = menu_01 + ("{:25}{:25}{:>10}\n".format(name, address, number))
                print(menu_01)
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
                    numbers = ""
                    number_count = int(number_count)
                    for i in range(1,number_count + 1):
                        phone = input("Phone Number {}: ".format(i))
                        numbers = numbers + phone + "#"
                    contacts = contacts + name + "*" + address + "*" + numbers + ";"
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
        menu_03 = "Edit Contact".center(62,"*") + "\n"
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
            menu_03 = menu_03 + ("{}){:25}{:25}\n".format(i + 1, name, address))
        print(menu_03 + "{})Go Back".format(contacts.count(";")+1))
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
        menu04 = "Delete Contact".center(60,"*") + "\n"
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
            menu04 = menu04 + str(i + 1) + ")" + "{:25}{:25}\n".format(name, address)
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
        elif not int(opt) in range (1,5):
            print("Option is out of range")
            input("Press Enter to continue...")
        else:
            opt = int(opt)
            if opt == 4:
                flag_05 = False
                flag_00 = True
            elif opt == 1:
                search_name = input("Enter Name to search: ")
                sname = True
            elif opt == 2:
                search_address = input("Enter Address to search: ")
                saddress = True
            elif opt == 3:
                search_number = input("Enter Number to search: ")
                snumber = True
            exist = False
            while not exist and not opt == 4:
                start_find = 0
                end_find = 0
                for i in range(contacts.count(";")):
                    found_contact = ""
                    numbers = ""
                    if i == 0:
                        start_find = 0
                        end_find = contacts.find(";") + 1
                    else:
                        start_find = end_find
                        end_find = contacts.find(";", start_find + 1) + 1
                    contact = contacts[start_find:end_find]
                    first_spacing = contact.find("*")
                    second_spacing = contact.find("*", first_spacing + 1)
                    name = contact[:first_spacing]
                    address = contact[first_spacing + 1:second_spacing]
                    if contact.count("#") > 1:
                        start_phone = 0
                        end_phone = 0
                        for j in range(contact.count("#")):
                            if j == 0:
                                start_phone = second_spacing + 1
                                end_phone = contact.find("#", start_phone)
                            else:
                                start_phone = contact.find("#", end_phone) + 1
                                end_phone = contact.find("#", start_phone + 1)
                            number = contact[start_phone:end_phone]
                            numbers = numbers + number + "#"
                            if j == 0:
                                found_contact = ("{:25}{:25}{:>10}".format(name, address, number))
                            else:
                                found_contact = found_contact + ("\n{:>60}".format(number))
                    else:
                        number = contact[second_spacing + 1:contact.find("#")]
                        numbers =  numbers + number + "#"
                        found_contact = ("{:25}{:25}{:>10}".format(name, address, number))
                    if sname and name == search_name:
                        print("Found Contact:\n{}".format(found_contact))
                        input("Press Enter to continue...")
                        sname = False
                        exist = True
                    elif saddress and address == search_address:
                        print("Found Contact:\n{}".format(found_contact))
                        input("Press Enter to continue...")
                        saddress = False
                        exist = True
                    elif snumber:
                        start = 0
                        end = 0
                        for k in range(numbers.count("#")):
                            if k == 0:
                                start = contact.find("*", contact.find("*") + 1) + 1
                                end = contact.find("#", start)
                            else:
                                start = contact.find("#", end) + 1
                                end = contact.find("#", start + 1)
                            number = contact[start:end]
                            if number == search_number:
                                print("Found Contact:\n{}".format(found_contact))
                                input("Press Enter to continue...")
                                snumber = False
                                exist = True

                if not exist:
                    if sname:
                        print("Name doesn't exist")
                        input("Press Enter to continue...")
                    elif saddress:
                        print("Address doesn't exist")
                        input("Press Enter to continue...")
                    else:
                        print("Number doesn't exist")
                        input("Press Enter to continue...")
                    exist = True