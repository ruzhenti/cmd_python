
from User_interface import get_info as gi

info = gi()
def writing_txt ():
    file = 'Notebook_1.txt'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write((f'{info[0]},{info[1]},{info[2]},{info[3]}\n'))

def writing_1_txt ():
    file = 'Phonebook_1.txt'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(list(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n'))

