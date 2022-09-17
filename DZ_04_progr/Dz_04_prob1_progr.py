# Вычислить число π c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from math import pi

d =  int(input("Enter a number for the specified pi precision:\n"))
print(f'number pi for the specified precision {d} equals {round(pi, d)}')
