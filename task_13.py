N = int(input("give a number: "))
l1 = []
for n in range(N):
    if n**2 <= N:
        n2 = n**2
        l1.append(n2)
    else:
        break
    # print(n)
print(l1)
