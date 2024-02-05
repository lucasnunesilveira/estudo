'''Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.'''
import os

passagem = float(input("Qual o valor da passagem ? "))
km_rodados = int(input("Quantos Km(s) tem essa viagem ? "))
if km_rodados >= 200 :
    valor_total = passagem + (km_rodados*0.45)
    print("O valor total a pagar é {:.2f}".format(valor_total))
else:
    valor_total = passagem +(km_rodados*0.50)
    print("O valor total a pagar é {:.2f}".format(valor_total))

os.system("pause")