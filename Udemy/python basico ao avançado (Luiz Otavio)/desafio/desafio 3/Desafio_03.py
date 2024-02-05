while True:

    cpf = input("Digite um cpf : ")

    novo_cpf = cpf[:9]

    reverso = 10
    total = 0

    for v in range(19):
        if v > 8:
            v = v - 9

        total = total + int(novo_cpf[v]) * reverso

        reverso = reverso - 1
        if reverso < 2:
            reverso = 11

            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            novo_cpf = novo_cpf + str(digito)
    if cpf == novo_cpf:
        print("Valido!!")
    else:
        print("Invalido")
