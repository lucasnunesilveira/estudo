#5.4
import os
import time
numero_desejado = int(input("Qual numero voce deseja usar (inteiro): "))
x = 0
while x <= numero_desejado:
    if x % 2 == 1 :
        print(x)
        time.sleep(0.5)
    x = x + 1
os.system("pause")
