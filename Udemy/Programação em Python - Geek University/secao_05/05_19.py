n1 = int(input("Digite o primeiro numero: "))
if (n1 % 3 == 0 ) and (n1 % 5 == 0 ):
    print("Valor invalido ")
elif (n1 % 3 == 0) or (n1 % 5 == 0):
    print("Valor Correto")
else :
    print("Numero errado !")