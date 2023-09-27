def addTelephone(telephones: list):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    otchestvo = input("Введите отчество: ")
    telephone = input("Введите номер телефона: ")
    telephones.add("{} {} {} {}\n".format(last_name, first_name, otchestvo, telephone))

def findTelephone(telephones: list):
    name = input("Введите в поиск имя или фамилию, чей номер хотите найти: ")
    print(f"Что удалось найти по поиску '{name}'")
    for telephone in telephones:
        if str(telephone).find(name) != -1:
            print(telephone)

def deleteTelephone(telephones: list):
    name = input("Введите в поиск имя или фамилию, чей номер хотите удалить: ")
    for telephone in telephones:
        if str(telephone).find(name) != -1:
            telephones.remove(telephone)
    print(f"Данные с {name} удалены")