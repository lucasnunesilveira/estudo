'''Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA'''''
string_01= 'AATTGGAA'
string_02= 'TG'
nome = ''
for k in string_01:
    if k not in string_02:
        nome = nome + k
print(nome)