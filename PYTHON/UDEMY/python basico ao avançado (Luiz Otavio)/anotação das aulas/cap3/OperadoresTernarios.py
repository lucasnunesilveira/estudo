
# Operadores  Ternario
estado_do_log = True
# normal
if estado_do_log :
    msg= ' lalalala'
else :
    msg = ' nao estar logado '
print(msg)
#ternario

msg = 'ola mundo' if estado_do_log else 'Usuario precisa logar '
#cria a variavel   if verifica condição else valor da variavel

print(msg)

idade = int(input("qual sua idade:"))
msg = ' pode acesar' if idade >= 18 else 'não pode acessar'
print(msg)

#Operador OR

nome = input("Qual o seu nome :")

print(nome or  None or 0 or False or  'voce não digitou nada !!')
