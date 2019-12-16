# class_a = 20
# class_b = 22
# class_c = 19
class_a = int(input("how many students are in class \"A\"?  "))
class_b = int(input("how many students are in class \"B\"?  "))
class_c = int(input("how many students are in class \"C\"?  "))
sum_of_student = class_a + class_b + class_c
sum_of_desks = (sum_of_student + 1) // 2
print("For {} students, we need {} desks!" .format(sum_of_student, sum_of_desks))
