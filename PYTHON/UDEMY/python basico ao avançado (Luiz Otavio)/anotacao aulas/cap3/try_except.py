'''
try:
    a
    print(a)
except (IndexError, KeyError) as erros :
    print("Erro de indice ou chave")
except Exception as erros:
    print('serve pra qualquer tipo de error no programa ')
finally:
    print("executar independe do try e except ")

def dividir (n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error :
        print(f'log : {error}')
        raise

try:
    print(dividir(2,0))
except ZeroDivisionError as error:
    print(error)
'''
def divide(n1,n2):
    if n2 == 0 :
        raise ValueError("O segundo numero não pode ser zero ") # aqui você especifica o tipo do error
    return n1/n2

try:
    print(divide(1,0))
except ValueError as erro :
    print(erro)
divide(1,0)