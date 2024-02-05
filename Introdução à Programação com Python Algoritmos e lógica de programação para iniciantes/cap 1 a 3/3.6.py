import os
materia1 = float(input("qual o valor da primeira nota: "))
materia2 = float(input("qual o valor da segunda  nota: "))
materia3 = float(input("qual o valor da terceira nota: "))
media = (materia1+materia2+materia3)/3
if media >=7:
    print("passou por media !! ")
else:
    print("Não passou por media !!")
os.system("pause")
