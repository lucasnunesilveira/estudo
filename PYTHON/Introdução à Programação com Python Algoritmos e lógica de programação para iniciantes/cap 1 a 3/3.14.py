import os 
n1 = float(input(' quantos km pecorreu o carro :  '))
n2 = int(input('quantos dias ficou alugado o carro : ' ))
print( ' o valor a ser pago foi {:.2f}' .format ((n2 *60)+ (n1*0.6)))
os.system("pause")
