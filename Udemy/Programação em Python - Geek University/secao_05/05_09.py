salario = float(input("Digite o seu salario: "))
prestacao = float(input("Digite o valor da prestação:"))
if salario >= (prestacao*0.2):
    print("pode pagar")
else:
    print("não pode pagar")