import os 

n1 = float(input(' qual o valor da casa  : '))
n2 = float(input(' qual o valor do seu salario : '))
n3 = float(input(' em quantos anos queres pagar ? : '))

prest = n3*12
valorprest = n1 / prest

if (n2*0.7 > valorprest ) :
       print('Pode comprar pois o valor da prestação é  {:.2f} , o  do salario a pagar é {:.2f} '.format( valorprest , (n2*0.7)))
else :
       print('Você não pode comprar a casa ')

os.system("pause")

