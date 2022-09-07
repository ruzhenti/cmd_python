#5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
#*Пример:*
#
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
from math import sqrt
from math import floor

X1 = float(input('Введите координаты X1:'))
Y1 = float(input('Введите координаты Y1:'))
X2 = float(input('Введите координаты X2:'))
Y2 = float(input('Введите координаты Y2:'))
a=X1-X2
b=Y1-Y2
s=100*sqrt(a*a+b*b)
s_rounded=floor(s)
print (s_rounded/100)