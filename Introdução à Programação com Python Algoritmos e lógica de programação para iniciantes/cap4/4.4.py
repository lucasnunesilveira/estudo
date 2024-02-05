import os 
n1 = float(input('qual o valor do salario :'))

if n1 >1250 :
       print(' o seu novo salario é de {:.2f} , com aumento de 10%'.format(n1*1.10))
else :
       print(' o seu novo salario é  de {:.2f} , com aumento de 15%'.format(n1*1.15))

os.system("pause")
