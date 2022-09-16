# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# ---------------------------------------------------------

numbers3=[1.1, 1.2, 3.1, 5, 10.01]
numbers4=[]
numbers5=[]

for j in range (0,len(numbers3)):
    c=str(numbers3[j]).split(".")
    if len(c) != 1:
        numbers4.append(c[1])
   
for j in range (0, len(numbers4)):
    numbers4[j]='0.'+ numbers4[j]
    numbers5.append(float(numbers4[j]))
print (max(numbers5)-min(numbers5))
