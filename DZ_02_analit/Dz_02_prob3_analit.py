#Задайте список из n чисел последовательности (1 + 1\n)^n и выведите на экран их сумму.
# округлённую до трёх знаков после точки.
# Пример:

# Для n = 6 -> 14.072

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
nums = get_squerence(n)
print(round(sum(nums), 3))




