header = input("Введите заголовок: \t\t")
text = input("Введите текст:\nВместо ентер исрользовать ';' \n\t")

text_1 = text.replace(";","\n")
txt = open("{}".format(header), "w" )
txt.write(text_1)
txt.close()

stroki = int(text.count(";"))+1

words = text_1.split()

letters = 0
for x in words:
   letters += len(x)

# letters = []
# for x in words:
#     for y in x:
#         letters.append(y)

print(letters)
print(len(words))
print(stroki)
