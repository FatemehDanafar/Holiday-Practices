a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a+b > c and a+c > b and b+c > a:
    print("you can draw the triangle.")
else:
    print(" Sorry! you can not draw the triangle.")