#4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
a = int(input('задайте номер квадранта(четверти)'))
if (a==1):
    print (f"ОДЗ для {a} квадранта  X > 0 и Y > 0")
if (a==2):
    print (f"ОДЗ для {a} квадранта  X < 0 и Y > 0")
if (a==3):
    print (f"ОДЗ для {a} квадранта  X < 0 и Y > 0")
if (a==4):
    print (f"ОДЗ для {a} квадранта  X < 0 и Y > 0")