# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Enter numbers separated by spaces:\n").split()))
print(f"Source List: {lst}")
sec_lst = []
[sec_lst.append(i) for i in lst if i not in sec_lst]
print(f"List of non-repeating elements: {sec_lst}")