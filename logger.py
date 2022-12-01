from model import get_info as info
def read_contact():
    with open('phonebook.csv', 'r', encoding ='utf = 8') as f:
        return f.read()

def writing_scv(info):
    file = 'phonebook.csv'
    with open(file, 'a', encoding = 'utf = 8') as data:
        data.write(f' фамилия: {info[0]}; имя: {info[1]}; номер телефона: {info[2]}; описание: {info[3]}\n')

def writing_txt(info):
    file = 'phonebook.txt'
    with open(file, 'a', encoding = 'utf = 8') as data:
        data.write(f' фамилия: {info[0]}\n имя: {info[1]}\n номер телефона: {info[2]}\n описание: {info[3]}\n\n')
