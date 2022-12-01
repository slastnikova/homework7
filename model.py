def get_info():
    info = []
    last_name = input(' ввод фамилии: ')
    info.append(last_name)
    first_name = input(' ввод имя: ')
    info.append(first_name)
    phone_number = input(' ввод телефон: ')
    info.append(phone_number)
    description = input(' ввод описание: ')
    info.append(description)
    return info
