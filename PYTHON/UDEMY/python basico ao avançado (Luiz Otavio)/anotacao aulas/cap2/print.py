#primeira aula de python
#função print -- aula 09

print("lala la ", end=" ")
print("lucas" , "nunes" , sep="__")
print("051","441","990",sep=".",end="-")
print("19")
'''
texto - aula 10- String-
print("Ola mundo 'lalala' como mundo ") # \ ele faz o anular o proximo caracter ou o texto
print(r"ola mundo \n")# ele  o 'r' anula todos os itens de codigo dentro

#primitivos- aula 11 -  tipos "primitivos"
print(type("lalla"))
print(type(123123))
print(type(10 == 10))
print(type(78.98))

#exercicio 2
altura = 1.56
peso = 92
nome = 'lucas nunes'
imc = peso / (altura * altura)
print(f"O nome dele é : {nome}  o altura dele é {altura} o imc é  {imc:.2f} peso é {peso} Kg ")

'''

'''
#aula 23 len
usuario = input("Qual o seu nome: ")
senha = input("Qual sua senha: ")
qnt_caracter = len(usuario)
#print(f'O nome foi {usuario} e tem {qnt_caracter} de caracter ' , type(qnt_caracter))
print(f"O total digitado foi de {len(usuario)+ len(senha)}")

if qnt_caracter > 6 :
    print("Você foi cadastrado no sistema.")
else:
    print("Você não foi cadastrado pelo sistema ")
if condição :
    pass # serve para rodar o codigo sem precisa fazer o codigo so pra separa  a logica
    ... 
'''
