#minha solução

l1 = [(v,y) for v,y in enumerate(range(10))]
dicionario = dict(l1)
somatorio= [i for i in dicionario.values() ]
print(sum(somatorio))


#solução da udemy

carrinho =  []

carrinho.append(('produto', 10.45 ))
carrinho.append((('prduto1','30')))
carrinho.append(('produto2',40))

lista1= sum([float(y) for x,y in carrinho])

print(lista1)

