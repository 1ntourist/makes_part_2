str = input("введите слово: \n\t")
if str == str[::-1]:
    print("Слово {} полиндром!".format(str))
else:
    print("Слово {} не полиндром!".format(str))
