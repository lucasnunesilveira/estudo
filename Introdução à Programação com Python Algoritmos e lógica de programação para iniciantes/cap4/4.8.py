import os
n1 = float(input(' qual o primeiro numero :  '))
n2 = float(input(' qual o segundo numero : '))
es = int(input(' Se for \n 1-soma \n 2-subtração \n 3-multiplicação \n 4-divisao : '))
if  es == 1 :
       print ( ' A soma de {} com {}  é {:.2f} '.format(n1 , n2 , ( n1+ n2 )))
elif es == 2 :
       print(' a subtração de {} com {}  é {:.2f} '.format( n1 , n2 , ( n1 - n2)))
elif es == 3 :
       print(' a  multiplicação de {} com {} é {:.2f} '.format(n1, n2 , (n1*n2)))
elif es == 4 :
       print(' a divisão  de {} com {} é {:.2f} '.format(n1 , n2 , ( n1/n2)))
else :
       print('ERRO!!  ' )
os.system("pause")
