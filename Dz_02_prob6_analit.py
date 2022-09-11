# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# Пример

# -Для "abababb" и "aba" -> 2

a = input ("Enter string a: ")
b = input ("Enter string b: ")
count = 0
b_len = len(b)
for i in range(len(a)):
    if a[i:i+b_len] == b:
        count += 1
print("Number of occurrences:", count)