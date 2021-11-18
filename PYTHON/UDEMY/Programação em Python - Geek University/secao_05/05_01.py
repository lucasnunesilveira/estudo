'''
    faça um programa  que receba  dois numeros  e mostre  qual deles  é o maior
'''
n1 = float(input("Digite o primeiro numero : "))
n2 = float(input("Digite o segundo numero "))
if n1 == n2 :
    print("Os dois numeros são iguais ")
elif n1 > n2 :
    print(f"O primeiro ({n1}) numero maior que o segundo numero ({n2})")
else:
    print(f'O segundo  numero é  ({n2}) maior que o primeiro  ({n1})')
