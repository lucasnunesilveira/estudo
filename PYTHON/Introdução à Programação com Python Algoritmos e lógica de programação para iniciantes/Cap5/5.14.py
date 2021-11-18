import time
import os

somatorio = 0
w = 0
n1 = 0
media = 0

while True :
    n1 = int(input("Digite um numero  e digite zero ( 0 )para sair :"))
    if n1 == 0 :
        break
    somatorio = somatorio + n1
    w += 1
    media = somatorio / w

print(f"O valor do somatorio é {somatorio} e a media é {media:.2f}, e foram {w} alunos ")
time.sleep(0.8)
os.system("pause")
