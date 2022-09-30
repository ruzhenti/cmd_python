def view_book():
    print("просмотр")
    with open('handbook.txt', 'r', encoding="utf-8") as file:     
        return file.readlines()
def append_book(data):
    print ("добавить")
    data1="**".join(data)
    with open('handbook.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data1}**\n')
def export_book(formiat):
    print("экспорт book to ",formiat)
    if formiat==1:
        with open('handbook.txt', 'r', encoding="utf-8") as file_1:
            tmp2=",".join(file_1.readlines())
            tmp3=tmp2.split(",")
            sumstroka=""
            for j in range(0,len(tmp3)):  # выделить в функцию
                stroka=tmp3[j].split("**")
                a=["","","",""]
                for i in range (1,len(stroka)-1):
                    a[i-1]=stroka[i]
                tmp5=",".join(a)
                sumstroka=sumstroka+tmp5+"\n"
                print(sumstroka)
        with open('handbook2.txt', 'w', encoding="utf-8") as file_2:
                file_2.write(f'{sumstroka},\n')
    elif formiat==2:
        #print(" выдрать по строкам и сформир строки для записи")
        with open('handbook.txt', 'r', encoding="utf-8") as file_1:
            tmp2=",".join(file_1.readlines())
            tmp3=tmp2.split(",")
            sumstroka=""
            for j in range(0,len(tmp3)):
                stroka=tmp3[j].split("**")
                a=["","","",""]
                for i in range (1,len(stroka)-1):
                    a[i-1]=stroka[i]
                tmp5="\n".join(a)
                sumstroka=sumstroka+tmp5+"\n"+"\n"
                print(sumstroka)
        with open('handbook3.txt', 'w', encoding="utf-8") as file_2:
                file_2.write(f'{sumstroka},\n')

def import_book():
    imeafile=input ("имя файла, откуда берем, полное и с расширением txt ")
    print(imeafile)
    with open(imeafile, 'r', encoding="utf-8") as file_41:
        tmp41="".join(file_41.readlines())
        print(tmp41)
    


n=int(input ("что хотите? 1-просмотр,2-добавить,3-экспорт, 4-импорт, 0 - выход"))
if n==1:
    tmp1=view_book()
    print(tmp1)
elif n==2:
    zap=[]
    zap.append(input("Add surname "))
    zap.append(input("Add name "))
    zap.append(input("Add telefon number "))
    zap.append(input("Add comment "))
    append_book(zap)
elif n==3:
    zap3=int(input("введите формат для экспорта:  1-через зпт или 2-через строку "))
    export_book(zap3)
elif n==4:
    import_book()
else:
    print ("end ")
