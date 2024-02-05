'''Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da
 divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do
dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.'''
n1 = int(input("Digite  o divendendo(o valor que deve ser dividido) : "))
n2 = int(input("Digite o  divisor : "))
c = 0
print(n1)
print(n1-n2)
menos = n1-n2
k = n1//n2
while c <= k :
    menos = menos - n2
    print(menos)
    if(menos == 0):
        break
    c = c + 1