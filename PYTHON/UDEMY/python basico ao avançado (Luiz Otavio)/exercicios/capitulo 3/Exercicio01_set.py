# no jeito que  eu fiz #
import random
lista_maior = []
lista_maior_nova = []

lista_de_inteiro = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,1,3,4,5,1,2,3,4],
    [1,2,2,3,3,4,4,5,5,1],
    [1,2,3,4,5,6,2,2,3,3],
]
#jeito que eu fiz
'''
for i in range(10):
    lista_menor = []
    for k in range(10):
        x = random.randint(0,10)
        lista_menor.append(x)
    lista_menor.sort()
    lista_maior.append(lista_menor)

def tirar_iguais():
    global lista_maior_nova
    global lista_maior
    for k in lista_maior:
        nova_lista = set(k)
        nova_nova = list(nova_lista)
        lista_maior_nova.append(nova_nova)
    return lista_maior_nova

tirar_iguais()

print(lista_maior_nova)
'''

# no jeito que foi mostrado no udemy
def encontra_primeiro_duplicado(param_listar_de_inteiro):
    numero_check = set()
    primeiro_duplicado  = -1

    for numero in param_listar_de_inteiro:
        if numero  in numero_check:
            primeiro_duplicado = numero
            break

        numero_check.add(numero)
    print("aaa", primeiro_duplicado)
    return primeiro_duplicado

for lista_de_inteiro in  lista_de_inteiro:
    print(lista_de_inteiro,encontra_primeiro_duplicado(lista_de_inteiro))


