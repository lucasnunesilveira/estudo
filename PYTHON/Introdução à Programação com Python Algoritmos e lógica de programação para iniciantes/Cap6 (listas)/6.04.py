'''Exercício 6.4 O que acontece quando não verificamos se a lista está vazia antes de
chamarmos o método pop?'''
lista01 = []
lista01.pop()
print(lista01)

'''
Traceback (most recent call last):
  File "..../6.04.py", line 4, in <module>
    lista01.pop()
IndexError: pop from empty list
'''