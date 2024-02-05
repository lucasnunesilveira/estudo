from math import log
n1 = int(input("Digite um numero:"))
if n1 < 0:
    print("numero inválido")
else:
    print(f'O valor logatimo desse numero é : {log(n1,10):.3f}')