#6.1

nota= [0,0,0,0,0,0,0]

x = 0
somatorio = 0
media = 0

while x < 7:
    nota[x] = float(input("Digite a sua nota: "))
    somatorio = somatorio + nota[x]
    x = x + 1
media = somatorio / x
print(f'O valor da media foi :  {media} ')
print(nota)