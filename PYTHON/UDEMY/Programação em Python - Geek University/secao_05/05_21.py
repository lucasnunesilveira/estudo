print("Choose an option:")
print("1-Sum the  2 number.")
print("2-Difference between 2 numbers (highest to lowest).")
print("3-product between 2 numbers")
print("4-division between 2 numbers (the denominator cannot be zero)")
op = int(input("Option: "))
if op == 1:
    n1=float(input("number 1 = "))
    n2=float(input("number 2 = "))
    resultado = n1 + n2
    print(resultado)
if op ==2:
    n1 = float(input("number 1 = "))
    n2 = float(input("number 2 = "))
    if ( n1 > n2 ):
        resultado = n1 - n2
        print(resultado)
    else:
        print(n2-n1)
if op== 3:
    n1 = float(input("number 1 = "))
    n2 = float(input("number 2 = "))
    resultado = n1*n2
    print(resultado)
if op == 4:
    n1 = float(input("number 1 = "))
    n2 = float(input("number 2 = "))
    resultado = n1 / n2
    print(resultado)

