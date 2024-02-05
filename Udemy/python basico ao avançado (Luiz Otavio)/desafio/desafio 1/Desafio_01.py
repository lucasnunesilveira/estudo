
#Crie uma variavel para nome (str)  , idade ( int)
#Altura (float) e peso ( float)  de uma pessoa
#Obter o ano de nascimento baseado pela idade atual
#obter o IMC com duas casas decimais
#Exibir o texto com todas informação na tela

ANO_ATUAL = 2020

nome = input("Qual o seu nome: ")
idade = int(input("Qual sua idade: "))
altura = float(input("Qual a sua altura:"))
peso = float(input("Qual o seu peso: "))

imc = peso / (altura*altura)
ano_nascimento = ANO_ATUAL - idade

print(f'O nome é {nome}')
print(f'A idade é {idade}')
print(f'O ano de nascimento {ano_nascimento}')
print(f'Altura : {altura}')
print(f'Peso: {peso}')
print(f'IMC : {imc:.2f}')
