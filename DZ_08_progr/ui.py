import subroutin as sub

def rab():
    n=int(input ("что хотите? 1-просмотр,2-добавить,3-экспорт, 4-импорт, 0 - выход"))
    if n==1:
        tmp1=sub.view_book()
        for k in range(0, len(tmp1)-1):
            print(tmp1[k], end="")
    elif n==2:
        zap=[]
        zap.append(input("Add surname "))
        zap.append(input("Add name "))
        zap.append(input("Add telefon number "))
        zap.append(input("Add comment "))
        sub.append_book(zap)
    elif n==3:
        zap3=int(input("введите формат для экспорта:  1-через зпт или 2-через строку "))
        sub.export_book(zap3)
    elif n==4:
        sub.import_book()
    else:
        print ("окончательный выход еще раз 0")
    return n