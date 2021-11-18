def imposto (n1, n2):
    novo_valor = n1 + ((n2/100)*n1)
    return novo_valor

n1 = float(input("Qual o valor da mercadoria:"))
n2 = float(input("Qual o valor do imposto encima da mercadoria "))

resultado = imposto(n1,n2)

print(f'O valor da mercadoria é R$ {resultado}')
