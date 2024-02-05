try:
    radiano = float(input('Digite o radiano : '))
    angulo = (radiano*180)/ 3.14
    print(f'O valor do radiano e {radiano} e o valor do angulo é {angulo:.2f}° ')
except ValueError:
    print("Digite o valor valido se for decimal não use virgulas use ponto ")