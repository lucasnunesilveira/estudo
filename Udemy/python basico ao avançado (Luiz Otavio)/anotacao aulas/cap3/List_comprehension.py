
#List_compreehension

l1 = [ 1 ,3,2,5,2,1,4,5,7,8,10]
exemplo01 = [variavel  for variavel in l1]
exemplo02 = [variavel * 5 for variavel in l1]
exemplo03 = [(x,x2) for x in l1 for x2 in range(3)]

l2 = [ 'lucas' , 'joao', 'maria']
exemplo04 = [v.replace("a","PP").title()for  v in l2]

tuple = (
    ('chave', 'valor'),
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),

)
exemplo05 = [(y,x) for x,y in tuple]
exemplo05 = dict(exemplo05)

l3 = list(range(100))
exemplo06 = [v for  v in  l3 if v % 2 == 1]

exemplo07= [v if v % 2 == 1 else 'par' for v in l3]

print(exemplo07)
