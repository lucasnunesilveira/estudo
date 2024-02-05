'''Exercício 6.7 Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(()) OK
()()(()()) OK
()) Erro'''

l= []

while  True :
    saida = print("Aperte S para sair : ")
    if saida == 'S':
        break
    entrada = input("Digite a expresão pra se verificar: ")

    x = 0
    while x < (len(entrada)):
        if entrada in '(' and ')':
            l.append(entrada)
            print("Ok")
        else:
            print("Algo estar de errado !! ")
