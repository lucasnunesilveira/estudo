import  sys
import time

#interaveis
lista = [ 1,2,3,4,5,6]

print(hasattr(lista,'__iter__'))
#for v in lista: # ele transforma a lista em um interador
#    print(v)

lista = iter(lista )

print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista,'__next__')) # verifica se é um interador

#geradores sao procedimentos que precisa de muita memorias

lista = list(range(10))
print(sys.getsizeof(lista)) # ele mostra a quantidade de byte que ta sendo usando no certo procedimento

lista = list(range(1000000))

print(sys.getsizeof(lista))

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

print(g)
for v in g:
     print(v)
l1 = [a for a in range(10000)] #são listas geradas geradas , salvas em uma parte da memoria RAM 
l2 = (a for a in range(10000)) #gerador ,ele gera as informação , mas ele nao salva na memora , são informação volatil
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
