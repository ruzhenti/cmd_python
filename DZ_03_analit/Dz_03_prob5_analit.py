
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

def Fibonacci(k):
    if k in [1, 2]:                       
        return 1
    else:
        return Fibonacci(k-1) + Fibonacci(k-2)

def NegaFibonacci(k):
    if k == 1:                       
        return 1
    elif k == 2:                       
        return -1
    else:
        fig1, fig2 = 1, -1
        for i in range(2, k):
            fig1, fig2 = fig2, fig1 - fig2
        return fig2

list = [0]
figure = int(input('Enter any number: '))
for b in range(1, figure + 1):
    list.append(Fibonacci(b))
    list.insert(0, NegaFibonacci(b))
print(list)