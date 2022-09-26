#2-03 Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# первое решение с функцией
# k = int(input('Введите число: ')) 
# def get_squerence(k):
#     return [(1 + 1 / x)**x for x in range (1, k + 1)]
# nums = get_squerence(k)
# print(sum(nums))

# второе решеие с list comprehension
k = int(input('Введите число: ')) 
spisok=[(1+1/k)**k for k in range(1,k+1) ]
print(sum(spisok))