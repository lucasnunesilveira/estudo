'''Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês,
e você deve considerá-lo para o cálculo de juros do mês seguinte.'''
salario = float(input("Qual o seu valor do seu salario: "))
QUANTIDADE_MES = 5 #aqui você coloca a quantidade de messes que queres que o programa calcule
x = 0
novo_salario_com_juros = 0
incremento_total = 0
novo_salario_com_juros = 0
novo_salario_com_juros_total = 0

while x <QUANTIDADE_MES :
    juros = float(input("Qual do juros do mês:"))

    incremento = juros*salario
    incremento_total = incremento_total + incremento
    novo_salario_com_juros =incremento + salario
    novo_salario_com_juros_total = novo_salario_com_juros_total + novo_salario_com_juros

    print(f"O seu salario no mes {x+1} foi de {novo_salario_com_juros}")

    x = x + 1
print(f"O seu valor total de incremento foi : {incremento_total} , o valor total do salario sem os juros foram {salario*QUANTIDADE_MES}, o valor total recebido em dinheiro foi {novo_salario_com_juros_total}")


