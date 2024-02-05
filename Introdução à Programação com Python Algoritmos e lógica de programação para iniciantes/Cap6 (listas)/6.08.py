'''Exercício 6.8 Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar
a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
saída do while.'''
lista = [1,44,55,22,66,23,4423,332,34,234]
x = 1
while x < (len(lista)):
    escolha = int(input("Digite um numero inteiro( a ordem que foi colocado o numero ): "))
    if escolha in lista :
        print(f"{escolha} achado na posição {lista.index(escolha)}")
        break
    else:
        print(f"{escolha} não encontrado")
    x += 1