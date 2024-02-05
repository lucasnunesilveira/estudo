import os
import time
'''Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com
os elementos das duas primeiras.'''
lista01 = []
lista02 = []
lista03 = []

x = 0
constante = 3

while x<constante :

    nome = str(input("Nome: "))
    lista02.append(nome)
    idade = int(input("Idade: "))
    lista01.append(idade)
    lista03 = lista01 + lista02

    x += 1
    time.sleep(0.8)

print(f'a primeira lista é : {lista01} a segunda é {lista02} a terceira lista é {lista03}')
os.system("pause")