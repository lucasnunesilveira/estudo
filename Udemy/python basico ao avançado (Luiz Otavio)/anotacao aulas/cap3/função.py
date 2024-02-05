# função py
'''
def ola_mundo(msg = 'ola' , nome = "usuario"): #def nome_da_função (paramentro ou nome da favariavel ):
    print(msg ,nome)
    return f'{msg} {nome}'
ola_mundo()# quando não se coloca nada ele retorna o valor padrão da função
ola_mundo('lucas' , 'nunes')
ola_mundo('mariane', 'menezes')
ola_mundo('liscas','caoma')

def funcao (var):
    print(var)

def f1(n1,n2):
    resultado = print(n1/n2)
    return print(resultado)

def nome (nome_cliente):
    va1 = nome_cliente
    return print(va1) , f1
nome = input("qual o nome ")


lista = [ 1,2,3,4,5,6]
n1,n2,*n = lista
print(n1,n2)
print(*lista) #desepacontando a lista


'''
# *arg colocando quando nao se sabe a quantidade limite de argumento
# **kwargs sao coloca quando um argumento tem uma palavra chave que indentifica  nome= 'lucas'

def fun(*args, **kwargs):  # se coloca *args quando nao sabemos a quantidade maxima dos argumentos pra coloca na função ...

    print(args)
    print(args[4]) # o quarto item do index 4
    print(args[-1]) # ultimo item dos args
    print(args[2]) #localiza o index 2
    args = list(args) # um cast que transforma o args em uma lista
    print(args) # proprocional a lista
    print(kwargs) # proprocional "dicionario"
    idade = kwargs.get('idade')
    print(idade)

fun(1, 2, 3, 4, 5, 4, 5, 23, 32, 123, 22, 33, 11, 224, nome = 'Lucas' , endereco ="Rua X")


