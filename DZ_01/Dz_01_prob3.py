#3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
#*Пример:*
#
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

a = float(input('Введите координаты X:'))
b = float(input('Введите координаты Y:'))
if (a>0 and b>0):
    print ('1й квадрант')
if (a>0 and b<0):
    print ('4й квадрант')
if (a<0 and b<0):
    print ('3й квадрант')
if (a<0 and b>0):
    print ('2й квадрант')
if (a==0):  
    print ('ось Y (вертикальная ординат)')
if (b==0):  
    print ('ось X (горизонтальная абсцисс)')