list = input("\t\t\t\t\t\tВведите числа через запятую:\n\t").split(',')
positives = []
negatives = []
for i in list:
    i = int(i)
    if i > 0:
        positives.append(i)
    elif i == 0:
        continue
    else:
        negatives.append(i)
print("\tСписок с положительными числами: \n", "\t", positives)
print("\tСписок с положительными числами: \n", "\t", negatives)
