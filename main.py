from logger import logger
from logger_path import logger_path

# Каталог документов
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

# Перечень полок
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# Далее - рабочие функции:
# 1. Функция, которая спросит номер документа и выведет имя человека, которому он принадлежит
@logger
# @logger_path('log_file2.txt')
def people_name(doc_number):
    for doc in documents:
        if doc["number"] == doc_number:
            print('\n Владелец документа: ', doc["name"])
            break
    else:
        print('\n Документ с таким номером не найден.')


people_name("123")
