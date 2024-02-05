nome =input("Qual o seu nome :")
quant_caracter =  len(nome)

if quant_caracter <= 4 :
    print("Nome Curto ")
elif quant_caracter <= 6 :
    print("Seu nome é normal")
else :
    print("Seu nome é grande ")