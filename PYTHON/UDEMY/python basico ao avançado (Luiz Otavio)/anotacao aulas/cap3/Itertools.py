from itertools import count,combinations,permutations,product


#Se  não coloca o parametro de saida ele ficara com o loop infinito , um contador INFINITO
contador = count(start=10,step= 5)
#O Start conta como dentro , o step é o passo de de um numero para outro

#count

for v in contador:
    print(v)
    if v == 20 :
        break

#combinations

pessoas = [ 'lucas' , 'joao','maria','francisco','camila','dodoca']
for grupo in combinations(pessoas,6): # a ordem nao importa , (lucas , maria) = (maria , lucas)
    print(grupo)

#permutations
for grupo in permutations(pessoas,6): # a ordem importa , (lucas,maria) # (maria,lucas)
    print(grupo)

#product
for grupo in product(pessoas,repeat=2): # todas as combinção possiveis e aceitando repetição (lucas, lucas) ,(lucas,maria)
    print(grupo)

