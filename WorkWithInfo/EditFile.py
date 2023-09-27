def addTelephone(telephones: set):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    otchestvo = input("Введите отчество: ")
    telephone = input("Введите номер телефона: ")
    telephones.add("{} {} {} {}\n".format(last_name, first_name, otchestvo, telephone))

def findTelephone(telephones: set):
    name = input("Введите в поиск то, чьи номера хотите найти: ")
    print(f"Что удалось найти по поиску '{name}'")
    for telephone in telephones:
        if str(telephone).find(name) != -1:
            print(telephone)

