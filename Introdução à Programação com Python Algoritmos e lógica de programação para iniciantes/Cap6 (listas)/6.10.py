'''Exercício 6.10 Modifique o programa do exercício 6.9 de forma a pesquisar p e v
em toda a lista e informando o usuário a posição onde p e a posição onde v foram
encontrados.'''
x = 0
lista_01 = [1,323,423,423,1121,332,32,12,44,223,3,22]
while x < (len(lista_01)):
    p = int(input("Digite o primeiro valor :"))
    v = int(input("Digite o segundo valor :"))
    if p in lista_01 :
        print(f"O primeiro valor é : {p} , e se encontra no index é  {lista_01.index(p)}")
    if v in lista_01 :
        print(f"O segundo valor é : {v} , e o index é  {lista_01.index(v)}")
    else:
        print("Não se encontrar no Ranger")
    if (p in lista_01) == True and (v in lista_01) == True:
        break
    x += 1