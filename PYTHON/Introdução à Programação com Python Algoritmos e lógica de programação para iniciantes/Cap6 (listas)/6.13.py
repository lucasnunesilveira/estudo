'''Exercício 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior
temperatura, assim como a temperatura média.'''

T = [-100, -8, 0, 100, 2, 5, -2, -4]

somatorio = 0
minimo = T[0]
maximo = T[0]

for e in T :

    if e> maximo:
        maximo = e

    if e < minimo:
        minimo = e

    somatorio += e

media = somatorio / len(T)

print(f'A media foi {media}')
print(f'A maior numero foi {maximo}')
print(f'A menor numero foi :  {minimo}')
