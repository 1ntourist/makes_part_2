year = int(input("Введите год: "))
if year % 4 == 0:
    print("\t{} год высокосный!".format(year))
else:
    print("\t{} год не высокосный!".format(year))
