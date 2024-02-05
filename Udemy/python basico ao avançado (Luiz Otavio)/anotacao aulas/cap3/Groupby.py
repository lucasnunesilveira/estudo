from itertools import groupby,tee
alunos = [
    {'nome': 'lucas' , 'nota': 'A'},
    {'nome': 'francisco' , 'nota': 'B'},
    {'nome': 'gabriella' , 'nota': 'C'},
    {'nome': 'jaoao' , 'nota': 'D'},
    {'nome': 'renata' , 'nota': 'A'},
    {'nome': 'isabella' , 'nota': 'B'},
    {'nome': 'maria' , 'nota': 'B'},
    {'nome': 'joaona' , 'nota': 'C'},
    {'nome': 'dolclas' , 'nota': 'D'},
    {'nome': 'junior' , 'nota': 'F'},
]
ordena_funcao = lambda item: item['nota']
alunos.sort(key=ordena_funcao)
#for v in alunos:
#    print(v)
alunos_agrupados = groupby(alunos,ordena_funcao)

for v,k in alunos_agrupados:
    va1, va2 = tee(k) # ele faz a copia do interador , o v1 , v2
    print(f'Agrupamento {v}')

    quantidade = len(list(va1))
    print(f'{quantidade} tirou {v}')
    for g in va2 :
        print(g)
    print()