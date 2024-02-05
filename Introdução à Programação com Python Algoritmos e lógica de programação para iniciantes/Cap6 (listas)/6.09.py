'''Exercício 6.9 Modifique o exemplo para pesquisar dois valores. Em vez de apenas
p, leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro.'''
l = [1,44,55,22,66,23,4423,332,34,234]
x = 0

while x < (len(l)):
    escolha = int(input("Escolha o seu numero :"))
    escolha_1 = int(input("Escolha o segundo numero :"))
    if escolha in l :
        print(f"O valor da primeira escolhar estar dentro do Ranger  valor é {escolha} , seu index é {l.index(escolha)}")
    if escolha_1 in l:
        print(f"O valor da segunda escolha estar dentro do Range  valor é {escolha_1} e o seu index é {l.index(escolha_1)}")
    else:
        print("Fora do range")
    if (escolha in l) == True  and (escolha in l) == True:
         if (l.index(escolha)) < (l.index(escolha_1)):
                print("A primiera escolha se encontra antes da segunda escolha na lista pre existente ")
                break
         else :
                print("A segunda escolha esta na frente da primeira ")
    x += 1

