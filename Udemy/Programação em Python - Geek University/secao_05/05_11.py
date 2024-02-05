numero = str(input("Digite o valor :"))
somatorio = 0
for i in numero:
    k = int(i)
    somatorio = somatorio + k

if somatorio > 0 :
    print(somatorio)
else:
    print("numero Invalido")