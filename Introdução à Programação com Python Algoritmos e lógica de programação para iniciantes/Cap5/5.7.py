import os
import time

'''Modifique o programa anterior de forma que o usuário também 
digite o início e o fim da tabuada, em vez de começar com 1 e 10.'''

comeco = int(input("Digite o valor inicio  da tabuada : "))
fim = int(input("Digite o valor final da tabuada : "))
x = 0
while x <=  fim :
    print(comeco * x)
    x = x + 1
    if (comeco * x == (fim+comeco)):
        break
    time.sleep(0.8)
os.system("pause")
