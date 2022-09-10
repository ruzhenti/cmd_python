#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Введите число: ')) 

def get_squerence(k):
    return [(1 + 1 / x)**x for x in range (1, k + 1)]
nums = get_squerence(k)
print(sum(nums))