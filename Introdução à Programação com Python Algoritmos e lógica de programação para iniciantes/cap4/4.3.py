#4.3
import os
n1 = int(input(' digite o primeiro  numero :  '))
n2 = int (input(' digite o segundo  numero :  '))
n3 = int(input(' digite o terceiro  numero  :  '))
if (n1>n2>n3) or (n1== n2>n3)or (n1> n2 ==n3):
       print(' o numero {} é o maior numero . '.format(n1))
       print('o menor numero é {}.'.format(n3))
if (n2>n1>n3)or (n2 == n3 >n1) or (n2> n1 ==n3):
        print('o numero {} é o maior numero . '.format(n2))
        print('o menor numero é {}'.format(n1))
if (n3>n2>n1) or (n3 == n1 > n2)or (n3>n1==n2):
        print('o numero {} é o maior '.format(n3))
        print('o menor numero é {}'.format(n1))
os.system("pause")
       
