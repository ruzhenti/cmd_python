#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint

N = int(input('Enter  N: '))
numbers = []
for i in range(N):
    numbers.append(randint (-N,N))
print(numbers)

stroka = input('Enter index of the elements which product you wish to get separated with space: ')
multipliers=stroka.split(" ")

mult=1
for j in range (0,len(multipliers)):
    mult=numbers[int(multipliers[j])]*mult
print (mult)