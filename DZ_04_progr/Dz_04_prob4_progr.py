#4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#*Пример:*  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random 
def rd ():
    return random.randint(0,101)
print (rd())

k=int(input("введите к "))

i=0
a=[]
for i in range(0,k+1):
    a.append(rd())
    i=i+1
print (a)

b=[]
for j in range(0,k+1):
    stroka=str(a[j])+"*x^"+str(j)
    b.append(stroka)
    j=j+1
print (b)

result="+".join(b)
print (result)

f1 = open("reasult.txt", "w")
f1.write(result)
f1.close()