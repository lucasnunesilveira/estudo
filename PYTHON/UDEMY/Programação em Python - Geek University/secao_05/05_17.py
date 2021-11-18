base_maior = float(input("Digite o valor da base maior : "))
base_menor = float(input("Digite o valor da base menor : "))
altura = float(input("Digite o valor da altura: "))

if base_menor > 0  and base_maior > 0:
    area = ((base_menor + base_maior) * altura)/2
    print(f"O valor da Area é : {area} ")
else:
    print("Digite o valor valido")
