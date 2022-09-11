#Реализуйте алгоритм перемешивания списка.

import random
my_list=['m','i','x','t','u','r','e']
dlina=len(my_list)
print(f'original\t',my_list)
for j in range (0,dlina-1):
    ind_insert=random.randint(0, dlina-1)
    value=my_list.pop()
    my_list.insert(ind_insert,value)
print (f'jumbled   \t',my_list)
