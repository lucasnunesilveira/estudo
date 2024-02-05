
#posição [012345678910] positivos
texto =  'Python sr3'
#posição [10987654321] negativo

#print(texto[2]) # ele mostra o t
#print(texto[9])#ultimo termo
#print(texto[-1])#sempre o ultimo termo da string
#print(texto[1:4])#ele começa do 1 caracter ate o 4 caracter ( porem o 4 estar fora )
#print(texto[1::2])#( inicio : fim : pula [ o passo ])
#print(len(texto))#ler a quantidade de caracter que tem na palavra

maximo = len(texto)
x = 0
while x < maximo :
    print(texto[x])
    x = x + 1
