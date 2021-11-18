nome = input("Qual nome do aluno:")
idade = int(input("Qual idade do aluno "))
prova_01 = float(input("Qual nota da primeira prova:"))
prova_02 = float(input("Qual a nota da segunda prova: "))
media = (prova_01+prova_02)/2
nome_impresso = nome.title()
if media >= 6 and idade >= 18:
    print(f"nome : {nome_impresso}")
    print("Situação : Aprovado")
else:
    print(f'nome : {nome_impresso}')
    print("Situação : Reprovado")