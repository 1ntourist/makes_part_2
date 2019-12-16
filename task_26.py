list = input("Введите числа через запятую:\n\t").split(',')
evens = []
odds = []
for i in list:
    i = int(i)
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print("Сумма четных чисел равна: \t", sum(evens))
print("Сумма нечетных чисел равна: \t", sum(odds))
