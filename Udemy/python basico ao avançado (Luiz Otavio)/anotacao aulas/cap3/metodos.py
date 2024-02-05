import sys # aqui como é a  biblioteca toda , precisamos chama a biblioteca pra depois chamar a "função" desejada
from sys import platform # quando especifica o que vc quer importa dentro da biblioteca , nao precisa chamar ele com o ponto
print(platform)


#aqui coloca pra ser executado somente para  quando for executado dentro do aquivo de py
#se for chamado  em outra função essa parte de baixo não sera executado
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
# v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v
if __name__ == '__main__':
    print(f'*asdas')