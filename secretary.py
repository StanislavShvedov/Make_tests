documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    # your code
    result = None
    for doc in documents:
        if doc_number == doc['number']:
            result = doc["name"]
            break
        else:
            result = "Документ не найден"
    return result


def get_directory(doc_number):
    # your code
    result = None
    for key, value in directories.items():
        if doc_number in value:
            result = key
            break
        else:
            result = "Полки с таким документом не найдено"
    return result


def add(document_type, number, name, shelf_number):
    # your code
    new_dict = {}
    new_dict['type'] = document_type
    new_dict['number'] = number
    new_dict['name'] = name
    documents.append(new_dict)
    directories[shelf_number] = new_dict['number']
    return 'Добавлен новый документ'


if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))