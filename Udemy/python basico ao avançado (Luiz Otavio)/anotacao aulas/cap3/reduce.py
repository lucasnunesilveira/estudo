from dados import clientes, lista, estoque
from _functools import reduce

acumula = 0
for i in lista:
    acumula += i

#print(acumula)

soma_lista = reduce(lambda ac , i: i + ac , lista , 0)
soma_produtos = reduce(lambda pt, p:p['preço'] + pt , estoque,0 )
# nome de saida = reduce ( lambda pt , nome da varivel mais o comando , local de busca , inicio de ac )


print(soma_produtos / len(estoque))
