valor_mercadoria = float(input("Digite o  valor produto: "))
total_pagar = valor_mercadoria*0.90
valor_parcela = valor_mercadoria / 3
valor_comissao = total_pagar * 0.05 #valor se for a vista
valor_comissao_parcelado = valor_mercadoria* 0.05 #valor se for parcelado

print(f'o valor  da mercadoria é {valor_mercadoria:.2f}')
print(f'O valor das parcelas é {valor_parcela:.2f}')
print(f'O valor da comissão se for a vista {valor_comissao:.2f}')
print(f'O valor da comissao se for em parcelas {valor_comissao_parcelado:.2f}')
