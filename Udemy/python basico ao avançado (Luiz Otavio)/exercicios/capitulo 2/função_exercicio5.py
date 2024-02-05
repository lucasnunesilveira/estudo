#Crie uma função 1 que recebe uma funçãoo 2 como parametro e retorne  o valor  da
# função 2 executada.

def  ola_jovem():
    return 'Ola pessoal'

def mastre (funcao):
    return funcao()

executando = mastre(ola_jovem)
print(executando)