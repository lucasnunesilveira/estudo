print("Digite o numero correspondente a operação :")
op= int(input("1-soma\n2-divisão\n3-multiplicação\n4-subtração\nescolha:"))
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
if op == 1:
    print(f'O primeiro numero {n1}, o segundo numero {n2}, a soma é {n1+n2}')
elif op == 2:
    print(f'O primeiro numero {n1}, o segundo numero {n2}, a divisão é {n1/n2}')
elif op == 3:
    print(f'O primeiro numero {n1}, o segundo numero {n2}, a multiplicação  é {n1*n2}')
elif op == 4:
    print(f'O primeiro numero {n1}, o segundo numero {n2}, a subtração é {n1-n2}')
else:
    print(f"O valor INVALIDO !!! ")
