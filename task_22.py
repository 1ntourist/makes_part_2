a = input("введите f если вы вводите фаренгейты, или c если вы вводите цельсии: \t")
if a == "f":
    far = int(input("введите фаренгейты: "))
    cel = round((far -32) * (5/9))
    print("{} фаренгейт равно {} цельсий.".format(far, cel))
elif a == "c":
    cel = int(input("введите цельсии: "))
    far = round((cel*(9/5)) + 32)
    print("{} фаренгейт равно {} цельсий.".format(cel, far))
else:
    print("введите f или c!!!")
