mails = [".@.", "a@a.com"]
valid_mails = []

for i in range(len(mails)):
    valid_mail = True
    if mails[i].count("@") != 1:
        valid_mail = False
    else:
        user = mails[i][:mails[i].find("@")] + "."
        domain = mails[i][mails[i].find("@") + 1:] + "."
        start = 0
        end = 0
        for j in range(user.count(".")):
            if j == 0:
                start = 0
                end = user.find(".")
            else:
                start = end + 1
                end = user.find(".", start)
            segment = user[start:end]
            if len(segment) == 0:
                valid_mail = False
            elif not segment.isalnum():
                valid_mail = False

        start = 0
        end = 0
        for j in range(domain.count(".")):
            if j == 0:
                start = 0
                end = domain.find(".")
            else:
                start = end + 1
                end = domain.find(".", start)
            segment = domain[start:end]
            if len(segment) == 0:
                valid_mail = False
            elif not segment.isalnum():
                valid_mail = False

    if valid_mail:
        valid_mails.append(i)

for mail in valid_mails:
    print(mails[mail])
