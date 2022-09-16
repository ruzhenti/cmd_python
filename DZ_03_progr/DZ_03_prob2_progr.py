# # 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

def product_pairs(spisok):
    my_list=[]
    for j in range (0,int(len(spisok)/2)+len(spisok)%2):
        my_list.append(spisok[j]*spisok[len(spisok)-1-j])
    return my_list
    
numbers3=[2,3,4,5,6]
print ("list as in example  ",numbers3)
print ("product of pairs:  ",product_pairs(numbers3))