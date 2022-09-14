# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2]))


lst = [2, 3, 5, 9, 3]
def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Sum is equal to: {s}")

sum_odd_index(lst)
lst = list(map(int, input("Enter the numbers separated by a space:\n").split()))
sum_odd_index(lst)

