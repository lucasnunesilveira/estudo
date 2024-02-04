casos = int(input(""))
for k in range(casos):
    lista_str = input("").split(" ")
    lista_inteiro = [int(i) for i in lista_str if i != '']
    
    contador = 0
    media = 0
    calculo = 0 
    media = sum(lista_inteiro[1:])/lista_inteiro[0]

    for i in lista_inteiro[1:]:
        if i > media:
            contador = contador + 1

    calculo = (contador * 100) / lista_inteiro[0]
    print(f"{calculo:.3f}%")