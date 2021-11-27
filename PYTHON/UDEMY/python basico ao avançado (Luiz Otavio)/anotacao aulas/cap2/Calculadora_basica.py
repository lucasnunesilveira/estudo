#Calculadora Basica

while True:
    print()
    x1 = input("digite o primeiro numero : ")
    x2 = input("digite o segundo numero :")
    op= input("digite um operador: ")
    if not  x1.isnumeric() or not x2.isnumeric():
        print("O valor invalido !!!")
        continue
    x1 =  int(x1)
    x2 = int(x2)
    if op == '+' :
        print(f'O resultado foi {x1+x2}')
    elif op == '-':
        print(f'O resultado foi {x1-x2}')
    elif op == '*':
        print(f'O resultado foi {x1*x2}')
    elif op == '/':
        print(f'O resultado foi {x1/x2}')
    else :
        print("digite o valor valido ")
    escolha = input("deseja sair ? ( y = sim n = não )")
    if escolha == ('y' or 's' or 'yes' or 'sim'):
        break
