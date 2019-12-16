list = list(input("Введите список (через пробел): \n").split())
element = input("Введите искомый элемент: \n")
el = list.count(element)
print("Элемент {} встречается в списке {} раз(а).".format(element, el))
