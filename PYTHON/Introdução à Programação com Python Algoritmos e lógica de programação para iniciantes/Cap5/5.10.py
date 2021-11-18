import os
import time
q = 1
p = 0
while q <= 10:
    r = input(f"Reposta do quesito {q} : ")
    if q == 1 and (r == "a" or r == "A") :
        p = p + 1
    if q == 2 and (r == "a" or r == "A" ):
        p = p + 1
    if q == 3 and (r == "c" or r == "C") :
        p = p+1
    if q == 4 and (r == "d" or r == "D") :
        p = p +1
    if q == 5 and (r == "e" or r == "E") :
        p = p +1
    if q == 6 and (r == "d" or r == "D") :
        p = p + 1
    if q == 7 and (r == "a" or r ==  "A") :
        p = p + 1
    if q == 8 and (r == "a" or r == "A") :
        p = p + 1
    if q == 9 and (r == "k" or  r == "K") :
        p = p + 1
    if q == 10 and (r == "a" or r == "A") :
        p = p + 1
    q = q + 1
print(f"o aluno fez {p} ponto(s)")
os.system("pause")
