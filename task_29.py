text = input("Введите текст: \t").split()
print(text)
stroka = ""
spisok = []
for i in text:
    for x in i:
        if x.isalnum():
            stroka += x
        else:
            stroka += " "
        spisok.append(stroka)
        stroka = " "

for x in spisok:
    print(x, end="")

#КОПИПАСТ
