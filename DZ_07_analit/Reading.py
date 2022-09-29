
from User_interface import get_info as gi

info = gi()

def reading_txt ():
       with open ('Notebook.txt', 'r', encoding = 'utf-8') as file:
           data = file.read()
       return data   

def reading_1_txt ():
        with open ('Phonebook.txt', 'r', encoding = 'utf-8') as file:
             data = file.read()
        return data