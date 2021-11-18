string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10

#aqui serve pra coloca na string separado em 10 em 10 visto que a repetição é em 10 em 10
#e o for pra fazer  interação dentro da string

ll = len(string)
print(ll)
objeto_de_analise = [ string[i: i+n] for i  in range(0, len(string), n ) ]
retorno = '.'.join(objeto_de_analise)
print(objeto_de_analise)
print(retorno)


# outra possivel solução vindo do aluno Rafael

string = '0123456789012345678901234567890123456789'
grupoOrdenado = ''.join(sorted(list(set(string))))
numeroDeGrupos = int(len(string) / len(grupoOrdenado))
lista = [grupoOrdenado for x in range(numeroDeGrupos)]
stringRetorno = '.'.join(lista)
print(lista)
print(stringRetorno)
