age = int(input("give your age: "))
list = list(range(age+1))
list_1 = []
if age % 2 ==0:
    for n in list:
        if n % 2 == 0:
            list_1.append(n)
    print(list_1)
elif age % 2!= 0:
    for n in list:
        if n % 2 != 0:
            list_1.append(n)
    print(list_1)
