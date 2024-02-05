from dados import lista,estoque,clientes
import  metodos
from  itertools import groupby

nova_lista = list(map(lambda  x : x *3 , lista))

#print(nova_lista)

def aumento(p):
    p['preço'] = round(p['preço'] *1.05,2)
    return p

precos = map(aumento,estoque)

#for preco in precos:
#    print(preco)



nomes = map(lambda p : p['nome'],clientes)
for k in nomes:
    print(k)