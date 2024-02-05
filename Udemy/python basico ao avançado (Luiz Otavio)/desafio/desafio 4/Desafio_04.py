# puxa a indentação Shft + tab
from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero

reverso = 10
total = 0

# verfificação do for
for v in range(19):
    if v > 8:
        v = v - 9

    total = total + int(novo_cpf[v]) * reverso

    reverso = reverso - 1
    if reverso < 2:
        reverso = 11

        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf = novo_cpf + str(digito)

print(novo_cpf)
'''

sequencia = novo_cpf == str(novo_cpf[0]) * 11

if cpf == novo_cpf and not sequencia :
    print("Valido!!")
else:
    print("Invalido" )
'''
