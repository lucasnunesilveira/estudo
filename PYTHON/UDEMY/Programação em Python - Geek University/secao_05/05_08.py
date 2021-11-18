nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
if  (nota1> 0 and nota1 <= 10) and (nota2>=0 and nota2<= 10) :
    media = (nota1 + nota2)/2
    print(f'A nota 1 = {nota1}\nA nota 2 = {nota2}\nmedia = {media}')
else:
    print("NOTA INVALIDA")

