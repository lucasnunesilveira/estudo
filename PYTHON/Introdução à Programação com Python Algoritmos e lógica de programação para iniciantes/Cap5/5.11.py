#5.11
'''Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.'''
import time
import os

deposito = float(input(f"Qual o valor inicial do mes : "))
juros = float(input("Qual o valor  qual a taxa de juros :" ))
x = 0
valor_total = 0
sem_juros = 0
pagamento_mensal = 0
QUANTIDADE_MES = 5

while x < QUANTIDADE_MES :

    acremento = deposito*juros*x
    novo_valor = deposito + acremento
    valor_total = valor_total + novo_valor
    print(f"O valor no mes do mes {x} : " ,deposito + acremento)
    sem_juros = deposito * x
    time.sleep(0.8)
    x = x + 1

print(f"O valor total com juros é : {valor_total} o valor so dos acremento é : {acremento} o valor sem acremento é : {sem_juros}")
os.system("pause")