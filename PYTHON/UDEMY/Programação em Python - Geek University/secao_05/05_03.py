'''
    leia um numero real . Se for positivo  imprima  imprima o numero em quadrado ,se for negativo
    eleve ele ao quadrado
'''
n1 = float(input("Digite o o numero que você deseja :"))
if n1 ==  0 :
    print("O valor escolhido é Zero (0). ")
elif n1 > 0 :
    raiz = n1 ** 0.5
    print(f"O valor do numero é {n1} e sua raiz é {raiz:.2f}")
else:
    quadrado = n1 * n1
    print(f"O valor do numero  é {n1:.2f} e o numero é {quadrado:.2f}")