#Exercício 6.6 Modifique o programa para trabalhar com duas filas. Para facilitar
#seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento
#da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.


ultimo_a = 4
ultimo_b = 4
fila_a = list(range(1, ultimo_a+1))
fila_b = list(range(1,ultimo_b+1))
l_total = []
l2 =[]
x = 0
y = 0

while True:

     print(f"Existem  na fila A {len(fila_a)} clientes na fila")
     print(f"Existem  na fila B {len(fila_b)} clientes na fila")
     print(f"Faltas as pessoas de ordem (fila A):  {sorted(fila_a)} lugar  ")
     print(f"Faltas as pessoas de ordem (fila B):  {sorted(fila_b)} lugar ")
     escolha_add = input("Escolha F para a fila 1 e G para fila 2 (Chegada de cliente) :")
     escolha = input("Escolha A para atendimento na fila 1 e B para atendimento na fila 2 e digite S pra sair: ")
     if escolha == 'S':
          break

     #adiciona na lista A e na lista B

     maximo_add= len(escolha_add)

     l2 = []
     y = 0

     while y < maximo_add:
          l2.append(escolha_add[y])

          if escolha_add[y] == 'F':
               ultimo_a += 1
               fila_a.append(ultimo_a)

          if escolha_add[y] == 'G' :
               ultimo_b += 1
               fila_b.append(ultimo_b)

          y += 1

     maximo=len(escolha)

     #aqui iniciar a parte do Atendimento ao cliente das filas A e B

     l_total  = []
     x= 0

     while x < maximo:
          l_total.append(escolha[x])
          x += 1
     print(l_total)

     if (len(fila_a)) == 0:
          print("Não tem ninguem na fila :")

     if 'A' in l_total :
          if (len(fila_a)) > 0 and (l_total.count('A')) > 0:

               l_total.count('A')
               atendimento_a = l_total.count('A')
               x= 0

               while x < atendimento_a:
                    if (len(fila_a)) == 0 :
                       continue
                    fila_a.pop(0)
                    print(f"Cliente da fila A : {x+1} atendido")
                    x += 1


     if (len(fila_b)) == 0 :
          print("Não tem ninguem na fila")

     if 'B'in l_total:

          if (len(fila_b)) > 0 and  (l_total.count('B')) > 0:

               l_total.count('B')
               atendimento_b = l_total.count('B')

               x = 0
               while x < atendimento_b :
                    if (len(fila_b)) == 0 :
                       continue
                    fila_b.pop(0)
                    print(f"Cliente da fila B : {x+1} atendido ")
                    x += 1
