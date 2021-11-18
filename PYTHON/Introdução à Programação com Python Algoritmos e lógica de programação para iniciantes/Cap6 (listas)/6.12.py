'''Exercício 6.12 Altere o programa da listagem 6.33 de forma a imprimir o menor
elemento da lista.'''
L=[13,7,2,4,1,-99]

minimo=L[0]

for e in L:
    if e < minimo :
        minimo = e

print(minimo)