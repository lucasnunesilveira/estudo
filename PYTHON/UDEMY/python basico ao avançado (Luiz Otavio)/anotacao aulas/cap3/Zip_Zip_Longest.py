from itertools import  zip_longest,count

cidade = [ 'São Paulo', 'Belo Horizonte', 'Recife', 'Nova Descoberta']
estados =['SP', 'MG','PE']

cidade_estados = zip(cidade,estados) #geradores

print(cidade_estados)

for v in cidade_estados:
    print(v)

cidade_estados = zip_longest(cidade,estados, fillvalue='Estados_BR')
print(dict(cidade_estados))

indice = count()

cidade_estados = zip(
    indice,
    estados,
    cidade
)

for x,y,z in cidade_estados:
    print(x,y,z)
