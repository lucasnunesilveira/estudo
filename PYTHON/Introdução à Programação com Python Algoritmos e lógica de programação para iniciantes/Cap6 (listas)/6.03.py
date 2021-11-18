'''Exercício 6.3 Fuaaça um programa que percorra ds listas e gere uma terceira sem
elementos repetidos.'''

lista01 = []
lista02 = []
lista03 = []

x = 0

while x < 5 :

    nome = str(input("Qual o nome dele: "))
    if nome not in lista01 :
        lista01.append(nome)
    idade = int(input("Qual sua idade: "))
    if idade not in lista02:
        lista02.append(idade)
    x += 1

lista02.sort()
lista01.sort()

lista03.extend(lista01 + lista02)


print(lista01 , lista02 , lista03 )