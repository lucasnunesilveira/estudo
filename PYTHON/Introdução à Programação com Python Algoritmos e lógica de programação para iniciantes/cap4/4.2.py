import os 
n1 = int(input('qual a velocidade do carro : '))
if n1 > 80 :
       print('acima da velocidade , sera multado , sua multa é  de {} reais '.format((n1- 80)*5))
if n1 < 80 :
        print('pode seguir tranquilo boa viagem ')
if n1 == 80 :
       print(' cuidado você ta no limite da velocidade maxima permitida na via ')
os.system("pause")
