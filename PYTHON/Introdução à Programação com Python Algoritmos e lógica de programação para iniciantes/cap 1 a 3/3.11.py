import os 
mercadoria = float(input('o valor da mercadoria é  : ' ))
desconto = float(input('o valor do desconto é  0 a 0.99 : ' ))

print('o valor da mercadoria é {} , o valor do desconto é {} , e o valor novo é {} '.format(mercadoria,desconto, mercadoria - (desconto*mercadoria) ))
os.system("pause")
