import os
import time

valor = 0

while True :

    n1 = int(input("Digite uma opção :\n1- 0,50 \n2- 1,00 \n3- 4.00 \n5- 7,00 \n9- 8,00: "))

    n2 = int(input("digite a quantidade do produto(Digite 0 para sair): "))

    if n1 == 0 or n2 == 0:
        break
    elif n1 == 1:
        valor = valor +( 0.50*n2)
    elif n2 == 2 :
        valor =valor = valor +( 1.00*n2)
    elif n2 == 3 :
        valor =valor = valor +( 4.00*n2)
    elif n2 == 5 :
        valor =valor = valor +(7.00*n2)
    elif n2 == 9 :
        valor =valor = valor +(8.00*n2)
    else:
           print("Valor invalido !!!")
    time.sleep(0.7)
print(f"O valor total da compra foi {valor} reais ")

os.system("pause")