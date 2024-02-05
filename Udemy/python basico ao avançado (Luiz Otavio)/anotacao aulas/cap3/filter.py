from dados import lista,estoque,clientes

nova_lista = list(filter(lambda  x : x>4 , lista))
nova_lista2 = [ x for x in lista if x>5]

def produto_caro(clientes):
    if clientes['idade'] >18:
        return True

produtos_caros = list(filter(lambda x : x['preço'] > 300 ,estoque))
pessoas_maiores = list(filter(produto_caro,clientes))
#print(pessoas_maiores)

for l in pessoas_maiores:
    print(l)

for v in produtos_caros:
    pass
    #print(v)
