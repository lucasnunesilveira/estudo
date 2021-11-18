#considerando duas listas inteiros ou float ( lista A e lista B)
#some o valores  nas listas retornando  uma nova lista  com os valores  somados :

#Exemplo
    #lista 1 = [ 1,2,3,4,5,6,7]
    #lista_2 = [1,2,3,4]
    #lista gerada = [2,4,6,8]

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4,5]

#modo pythonico

adicionar1 = [x + y for x , y  in zip(lista2,lista2)]
print(adicionar1)


#modo comum


nova_lista = zip(lista2,lista2)
nova = []

for (x,y) in nova_lista:
    adicionar = x+y
    nova.append(adicionar)
print(nova)

