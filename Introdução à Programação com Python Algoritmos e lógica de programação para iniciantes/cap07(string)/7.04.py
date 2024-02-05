'''Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x'''

String = 'TTAAC'
print(f"A quantidade que a letra C aparece é de {String.count('C')}x")
print(f"A quantidade que a letra A aparece é de {String.count('A')}x")
print(f"A quantidade que a letra T aparece é de {String.count('T')}x")