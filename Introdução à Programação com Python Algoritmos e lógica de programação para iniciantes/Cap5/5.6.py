'''Altere o programa anterior para exibir os resultados no mesmo formato
de uma tabuada: 2x1 = 2, 2x2=4, ...'''
import time
import os

entrada_01 = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(f"O valor da multiplicação de {x} X {entrada_01} : ", entrada_01 * x)
    time.sleep(0.5)
    x = x + 1
os.system("pause")
