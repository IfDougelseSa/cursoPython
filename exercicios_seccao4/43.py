# Ajuda vendedores
valor = float(input('Digite o valor: '))

desconto = valor * 0.9
parcela = valor / 3
comissao = (desconto) * 0.05
comissao_parcelado = valor * 0.05

print(f'{desconto}, {parcela}, {comissao}, {comissao_parcelado}')
