'''

Faça uma lista de tarefas com  as seguintes opção :
    Adicionar tarefa
    listar tarefa
    opção de desfazer ( a cada  vez  que chamamos  , desfazer a ultima ação )
    opção de refazer ( a cada  vez  chamarmos, refaz  a ultima  ação )

'''
import  time
import os

def mostrar_tarefa ():#2
    print("\n tarefa :")
    print(agenda_tarefa)
    print()
    print("Verificado com sucesso ")
    time.sleep(0.8)



def adicionar_pessoas ():#1
    adicionar = input("O que vc deseja adicionar na lista de fazeres: ")
    agenda_tarefa.append(adicionar)
    print("Adicionado com sucesso !! ")
    time.sleep(0.8)


def remover_nome (agenda_tarefa,agenda_de_repor):
    if not agenda_tarefa:
        print("não tem nada ")
        return
    ultimo_item = agenda_tarefa.pop()
    agenda_de_repor.append(ultimo_item)
    print("Realizado com sucesso !!! \n ")
    time.sleep(0.8)
    


def refazer(agenda_tarefa,agenda_de_repor):
    if not agenda_de_repor:
        print("não tem nenhuma alteração ")
        return
    ultimo_refazer = agenda_de_repor.pop()
    agenda_tarefa.append(ultimo_refazer)
    print('realizado com sucesso ')
    time.sleep(0.8)


agenda_tarefa = ['pegar chocolate', 'comprar pao ']
agenda_de_repor = [ ]
if __name__ == '__main__':
    while True:
        print("1-Adicionar tarefa")
        print("2-Listar as tarefas")
        print("3-Desfazer alguma tarefa")
        print("4-Refazer alguma tarefa")
        print("5-Sair do programa")
        op = int(input("Qual a opção :"))

        if op == 1 :
            adicionar_pessoas ()

        if op == 2 :
            mostrar_tarefa ()

        if op == 3 :
            remover_nome (agenda_tarefa,agenda_de_repor)

        if op ==4  :
            refazer(agenda_tarefa,agenda_de_repor)

        if op == 5 :
            break


