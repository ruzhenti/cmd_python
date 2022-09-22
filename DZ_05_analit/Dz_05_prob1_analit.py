
# Напишите программу, удаляющую из текста все слова, содержащие ""абв""


f1 = open("my_file.txt", "r", encoding="utf-8") 
text = f1.readline()
f1.close()
print(text)   # Пищеваяабв ценность ( средниеабв значения ) в 100 г продукта: жирыабв, белки, углеводыабв'
print( " ".join(filter(lambda x: "абв" not in x, text.split())))

f2 = open("my_file_out.txt","w")
f2.writelines(text)
f2.close()
