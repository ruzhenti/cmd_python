# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или боле чем имеется в куче.
# b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. 
# Достаточно довести игру до такой ситуации.

from random import randint

def input_dat(name):
    x = int(input(f"{name}, enter the number of candies you will take from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter the correct number of candies: "))
    return x


def p_print(name, k, counter, value):
    print(f"Went {name}, he took {k}, now he has {counter}. left on the table {value} candies.")

player1 = input("Enter the name of the first player: ")
player2 = input("Enter the name of the second player: ")
value = int(input("Enter the number of candies on the table: "))
flag = randint(0,2) 
if flag:
    print(f"The first one walks {player1}")
else:
    print(f"The second one walks {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Won {player1}")
else:
    print(f"Won {player2}")