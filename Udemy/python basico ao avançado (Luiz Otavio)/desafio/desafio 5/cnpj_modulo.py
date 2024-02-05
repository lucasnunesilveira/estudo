import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def validade(cnpj):
    cnpf = tratamento(cnpj)
    if repetitivos(cnpj):
        return False

    novo_cnpj = calcular_digito(cnpj=cnpj,digito=1)

def calcular_digito(cnpj,digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
    elif digito == 2:
        regressivos = REGRESSIVOS
    else:
        return  None
    total = 0

    for indece ,regressivo  in enumerate(REGRESSIVOS):
        print(indece,regressivo)

#verifica se o cnpj tem os numeros repetitivos
def repetitivos(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    #print(sequencia)
    if sequencia == cnpj:
        return True
    else:
        return False

#tratamento feito pelo CNPJ - OK
def tratamento(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
