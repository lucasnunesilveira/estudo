from pessoas import Pessoas

# p1(o nome da pessoa )  = o nome da pessoa  . chama a função que quer ser executada

# name = input("What's your name ?")


p1 = Pessoas("lucas", 27)  # aqui ele pede no ( nome = lucas ) , ( idade = 26 )
p2 = Pessoas("doroca", 42)  # aqui ele pede no ( nome = lucas ) , ( idade = 26 )

p1 = Pessoas.por_ano_nascimento('lucas',1994)
print(p1)
print(p1.idade)
p1.get_ano_nascimento()
