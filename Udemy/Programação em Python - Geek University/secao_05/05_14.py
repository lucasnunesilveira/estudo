nota_lab = float(input("nota lab: "))
nota_ava = float(input("nota da avaliação Semeestral : "))
nota_final = float(input("nota da avaliação final : "))
media = (( nota_lab * 2)+(nota_ava * 3)+(nota_final  * 5))/10
if (nota_final >= 0  and nota_final <= 10) and (nota_lab >= 0 and nota_lab <= 10) and (nota_ava >= 0 and nota_ava <= 10):
    if media >= 0  and media <= 2.9 :
        print("Reprovado")
    elif media > 2.9 and media <= 4.9:
        print("Recuperação")
    else :
        print("Aprovado")