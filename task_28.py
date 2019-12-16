list = input("\t\t\t\t\t\tВведите числа через запятую:\n").split(',')
list_1 = []
for i in list:
    i = int(i)
    if i > 0:
        list_1.append(1)
    elif i < 0:
        list_1.append(-1)
    else:
        list_1.append(0)
print("Ваш список: \n", "\t", list_1)
