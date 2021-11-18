'''Exercício 6.11 Modifique o programa da listagem 6.15 usando for. Explique por
que nem todos os while podem ser transformados em for.'''

L=[7,9,10,12]

p=int(input("Digite um número a pesquisar:"))

for e in L: # "e" igual uma variavel
    if e == p: # o se para ser a varivel do for , ele for igual um p  ( caso dor True)
        print("Elemento encontrado!")
        break
    else:# caso if nao deu certo , usou o else
        print("Elemento não encontrado.")
        break