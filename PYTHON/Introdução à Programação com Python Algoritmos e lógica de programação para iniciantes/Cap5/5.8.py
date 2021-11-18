'''Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação
de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''
import os
import time

x1 = int(input("O valor de entrada é : "))
x2 = int(input("O segundo valor : "))
co = 2
while co <= x1  :
    print(f'{x2}+',end="")
    co= co + 1
    time.sleep(0.8)
print(x2)
os.system("pause")
