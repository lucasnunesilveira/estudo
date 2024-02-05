import os 
n1  = float(input(' qual o valor do seu salario  :  '))
n2 = float(input(' qual o valor do aumento de(0  a 1 onde o 0 igual a 0% e 1 igual a 100%):  '))
print('o valor do salario foi {} , o aumento foi de {} , e seu novo sario é {} .'.format(n1, n2 , n1*(1+n2)))
os.system("pause")
