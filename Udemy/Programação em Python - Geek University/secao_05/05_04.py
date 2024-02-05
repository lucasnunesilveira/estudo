'''
    Receba um numero se for positivo calcular o raiz quardada dele e a potencia dele
'''
n1 = float( input("Digite o numero : "))
if n1 == 0 :
    print(f"O valor é  digitado é Zero (0)")
elif n1  > 0 :
    raiz = n1 ** 0.5
    potencia = n1 * n1
    print(f"O numero digitado é {n1}\nA sua raiz é : {raiz}\nA potencia é {potencia}")
else:
    print(f"O valor é negativo")