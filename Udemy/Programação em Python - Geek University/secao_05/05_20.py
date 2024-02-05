side1 = float(input("side 1: "))
side2 = float(input("side 2: "))
side3 = float(input("side 3: "))
if side3 < side2 + side1 or side1 < side3 + side2 or side2 < side3 + side1:
    if side1 == side2 == side3:
        print("Is an equilateral Triangle")
    if side3 != side2 != side1:
        print("Is a scalene Triangle")
    if (side3 == side2 != side1) or (side2 == side1 != side3) or (side1 == side3 != side2):
        print("Is a isosceles Triangle")
else:
    print("Not a Triangle")
