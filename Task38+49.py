"""
Задача №49. Решение в группах
Создать телефонный справочние с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import WorkWithInfo.ReadAndWriteFile as rw
import WorkWithInfo.EditFile as ef
filename = "Telephone_list.txt"
telephones = list(rw.read_file(filename))

# Поиск
# ef.findTelephone(telephones)
# Добавление
# ef.addTelephone(telephones)
ef.deleteTelephone(telephones)
rw.write_in_file(filename, telephones)
