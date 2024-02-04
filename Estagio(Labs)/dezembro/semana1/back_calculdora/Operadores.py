def somar(a, b):
    soma = a + b
    return print(f"A soma foi {soma}")

def subtrair(a, b):
    x = a - b
    return print(f"O valor da Subtração é {x}")

def dividir(a, b):
    try:
        x = a / b
        return print(f"O valor da divisao é {x}")
    except ZeroDivisionError:
        print("Não Existe divisão por Zero ")
        raise   

def multiplicar(a, b):
    x = a * b
    return print(f"A multiplicar foi {x}")
