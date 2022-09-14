
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = ""
# n = int(input("Enter a number to convert decimal to binary:\n"))
# while n != 0:
#     a = str(n%2) + a
#     n //=2
# print(a)

n = int(input('Please input integer: ')) 
a = ''
while n > 0:
    a = str(n % 2) + a
    n = n // 2
print(f'Binary number: {a}')