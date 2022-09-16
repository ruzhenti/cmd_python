# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# ----------------------------------------------------------
def to_bin (a, osn):
    dv=[]
    while a > 0:
        bost=a%osn
        b4astn=a//osn
        bost_str=''.join(str(bost))
        dv.append(bost_str)
        a=b4astn
    dv.reverse()
    return ''.join(dv)

b=int(65)
osn_si=int(2)

print("десятичное ",b," в системе счисл. с основанием ",osn_si, " это: ",to_bin(b, osn_si))
