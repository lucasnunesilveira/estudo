altura = float(input("O valor da altura:"))
sexo = str(input("Qual sexo (masculino = M ) , (Feminino = F):"))
if sexo == "M":
    peso_ideal = (72.7*altura)-58
    print(f"O peso ideal é {peso_ideal:.2f}")
else:
    peso_ideal = (62.1*altura)-44.7
    print(f"O peso ideal é {peso_ideal:.2f}")
