def main(funcao,*args ,**kargs):
    return funcao(*args ,**kargs)

def fala_pessoal(nome):
    return f'{nome}'

def saudacao(nome,saudacao):
    #o valor parece na ordem que foi escrita
    return f'{saudacao} , {nome}'

#
executando = main(fala_pessoal,'Lucas')
executando1 = main(saudacao,'Lucas', saudacao= 'boa noite')
print(executando1)