# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  
# Негафибоначчи

k=8

list=[]
list.append(1)
list.append(1)
list.insert(0,list[1]-list[0])

for n in range (1,k-1):
    list.append(list[n]+list[n+1])

j=0
for n in range (1,k+1):
    list.insert(0,list[n-j]-list[n-1-j])
    j=j+1
print (list)
