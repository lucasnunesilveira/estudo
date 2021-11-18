'''Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas
as letras comuns a ambas.'''

string_01 = 'AAACTBF'
string_02 = 'CBT'
nome = ''
for k in string_01 :
    if k in string_02:
        nome = nome + k
print(nome)