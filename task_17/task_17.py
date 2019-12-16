try:
    name = input("Hello, what is your name? \n")
    print("\tHello, ", name.title())
    complaint = int(input("\nOn whom would you like to leave a complaint? \
        \n\t1 - Google Kazakstan\n\t2 - Google Paris\n\t3 - Google UAR\
        \n\t4 - Google Kyrgystan\n\t5 - Google San Francisco\
        \n\t6 - Google Germany\n\t7 - Google Moscow\n\t8 - Google Sweden \n"))
    googles = {1:'Google Kazakstan', 2:'Google Paris', 3:'Google UAR',
               4:'Google Kyrgystan',5:'Google San Francisco', 6:'Google Germany',
               7:'Google Moscow', 8:'Google Sweden'}

    if complaint in googles:
        print("\tHere you can leave a complaint on: {} ".format(googles[complaint]))
        txt = open("{}".format(googles[complaint]),'w')
        text = input("\n\tWrite here: \n\t")
        txt.write(text)
        txt.close()

    print("\n\tThanks for your feedback!!!")
except Exception:
    print("You have to choose!")
