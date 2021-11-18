
'''
#aula do while - 31 -

while True : # Loop infinito , visto que a condição True é totalmente explicita
    nome = input("Qual o seu nome :")
    print(f"o seu nome é {nome}")
'''

'''
# uso do continue 

x = 0

while x <= 10 :
    if x == 5 :
        x= x +1
        continue
    print(x)
    x = x + 1

'''

'''
#uso do break ,o uso do break serve para ele sair do laço e sair do programa .

x = 0
while x < 10 :
    if x == 5 : # quando ele chega no valor 5 ele finaliza a função do programa 
        break
    print(x)
    x = x + 1

'''

'''
#plano cartesiano 

x = 0
while x <= 10 :
    y = 0
    while y <= 5 :
        print(f'({x},{y})')
        y += 1
    x += 1
print("END")


'''