
def fizz_bizz (n1):

    if n1 % 3 == 0 and n1 % 5 == 0 :
        var1 = print("FIZZZ BIZZZ")
        return var1
    elif n1 % 3 == 0 :
        var1 =print("FIZZZ")
        return var1
    elif n1 % 5 == 0 :
        var1 = print("BIZZ")
        return var1
    return  n1

n1 = float(input("Digite um valor : "))

resultado = fizz_bizz(n1)
