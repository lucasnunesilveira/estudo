n1 = input("Digite um numero inteiro: ")
if n1.isdigit():
    n1 = int(n1)
    if n1 % 2 == 0 :
        print("O valor que você digitou foi par.")
    elif n1 % 2 == 1:
        print("O valor é impar.")
else:
    print("Valor invalido.")