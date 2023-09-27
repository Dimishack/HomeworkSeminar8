def addTelephone(telephones: set):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    otchestvo = input("Введите отчество: ")
    telephone = input("Введите номер телефона: ")
    telephones.add("{} {} {} {}\n".format(last_name, first_name, otchestvo, telephone))
    