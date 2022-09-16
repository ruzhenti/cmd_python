#1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def summ_odd(spisok):
    my_sum=0
    for j in range (1,len(spisok),2):
        #print (my_sum)
        my_sum=int((spisok[j]+my_sum))
    return my_sum
    
numbers2=[2,3,5,9,3]
print("list as in example  ",numbers2)
print ("sum of elements with odd indices:  ",summ_odd(numbers2))