# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.



def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

f1 = open("file55.txt", "r", encoding="utf-8") 
s = f1.readline()
f1.close()
print(f"Text after encoding: {coding(s)}")
print(f"Text after decryption: {decoding(coding(s))}")
f2=open("file66.txt","w")
f2.writelines(coding(s))
f3=open("file77.txt","w")
f3.writelines(decoding(coding(s)))