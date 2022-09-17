# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Enter the number: "))
i = 2 # first prime number
lst = []
N = n
while i <= n:
    if n % i == 0:
        lst.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Prime factors of a number {N} on the list: {lst}")
