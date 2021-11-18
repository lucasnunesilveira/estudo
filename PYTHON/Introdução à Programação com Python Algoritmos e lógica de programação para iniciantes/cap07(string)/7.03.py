'''Escreva um programa que leia duas strings e gere uma terceira apenas
com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
A ordem dos caracteres da terceira string não é importante.'''
string_01 = 'CTA'
string_02 = 'ABC'
nome = ''
for k in string_02:
    if k not in string_01:
        nome = nome + k
for k in string_01:
    if k not in string_02 :
        nome = nome + k
print(nome)
