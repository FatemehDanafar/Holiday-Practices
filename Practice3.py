m = int(input("Enter m please: "))
n = int(input("Enter n please: "))
def chess (n,m):
 for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0:
            print("*",end="")
        else:
            print("#",end="")
    print()
chess(n,m)    