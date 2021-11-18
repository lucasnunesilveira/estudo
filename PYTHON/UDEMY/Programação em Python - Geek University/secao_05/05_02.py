'''
    receba um numero  e calcule a raiz quadrada  se for positiva
'''
n1 = float(input(f"Digite o numero que deseja saber da raiz :"))

if n1 == 0 :
    print(f"O numero que vc escolheu {n1} e sua raiz é  0 ")
elif n1 > 0 :
    raiz = n1**0.5
    print(f"O numero {n1} e a raiz é {raiz:.2f}")
else:
    print("O numero não da pra fazer raiz no conjuntos dos numeros REAIS  ")
