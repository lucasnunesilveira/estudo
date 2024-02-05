n2 = input("Digite a hora em inteiro :")
if n2.isdigit():
    n2 = int(n2)
    if n2 >= 0  and n2 < 11 :
        print("Bom Dia")
    elif n2 >= 12 and n2 < 17 :
        print("Boa tarde")
    elif n2 >= 18 and n2 < 23 :
        print("Boa Noite")
    else:
         print("Valor invalido !!!")