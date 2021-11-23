from pessoas import Pessoas

# p1(o nome da pessoa )  = o nome da pessoa  . chama a função que quer ser executada
# name = input("What's your name ?")


p1 = Pessoas("lucas", 27)  # aqui ele pede no ( nome = lucas ) , ( idade = 26 )
p2 = Pessoas("doroca", 42)  # aqui ele pede no ( nome = lucas ) , ( idade = 26 )

p3 = Pessoas.por_ano_nascimento('lucas',1994)
print(p3) #aqui ele mostra a class onde estar no local da memoria
print(p3.nome, p3.idade)# ele calcula a idade pelo paramentro ano de nascimento
p3.get_ano_nascimento() #aqui ele executa a função
print("\naqui ele vai vai gerar na no metodo estatico")
print(Pessoas.gera_id())