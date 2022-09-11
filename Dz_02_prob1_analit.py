# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#-0,56 -> 11

float_num = input('input number: ')
sum = 0
for i in float_num:
    if i != '.' and i !='-':
        sum += int(i)
print(sum)

