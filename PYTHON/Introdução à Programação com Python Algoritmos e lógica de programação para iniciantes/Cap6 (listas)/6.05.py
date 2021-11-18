'''Exercício 6.5 Altere o programa da listagem 6.21 de forma a poder trabalhar com
vários comandos digitados de uma só vez. Atualmente, apenas um comando pode
ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
e, finalmente, a saída do programa.'''

ultimo =  4
fila = list(range(1,ultimo+1))
l1 = []
w = 0
a = 0

while True:

    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"È o : {sorted(fila)} lugar \n ")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")

    entrada = input("Operação (Digite tudo juntos F ,A e o S):")
    maximo =len(entrada)

    x = 0
    total_f= 0
    total_a = 0

    while x < maximo:
        l1.append(entrada[x])

        x += 1

        if 'A' in l1 :
            if (len(fila)) > 0 and (l1.count('A')) > 0:
                l1.count('A')
                atendido = l1.count('A')
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
                atendido = 0
            else:
                print("Fila vazia! Ninguém para atender.\n")
        if 'F'in l1 :
            ultimo += 1
            fila.append(ultimo)
        l1 = []
