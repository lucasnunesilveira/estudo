#exercicio 4.10
import os

n1 = float(input (' Quantos Kwh foram consumido  ? '))
n2 = int(input (' Qual o tipo de instalção : \n 1- R- Residencia \n 2 - I=industria \n 3-C = comercio : '))

if ( n1 <= 500 ) and ( n2 == 1) :
       print(' O valor a pagar é {} reais '.format(n1 * 0.4 ))
elif (n1 >500) and ( n2 ==1 ) :
       print(' O valor a pagar é {} reais '.format(n1*0.65))
elif (n1 <=  5000) and (n2 == 2):
       print('O valor a pagar é {} reais  '.format(n1*0.55))
elif (n1 > 5000) and ( n2== 2):
       print('O valor a pagar é {} reais '.format(n1*0.60))
elif (n1 <= 1000) and (n2 == 3 ):
       print('O valor a pagar é {} reais '.format(n1 *0.55))
elif (n1 > 1000) and ( n2 == 3 ):
       print( 'O valor a pagar é {} reais  '.format(n1*60))
else :
       print(" ERROO")

os.system("pause")
