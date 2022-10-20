from os.path import exists
from Csv_creating import creating
from File_writing import writing_scv
from File_writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()
print('Введенный Вами контакт сохранен в телефонный справочник в двух форматах в файлы Phonebook.txt и Phonebook.csv')