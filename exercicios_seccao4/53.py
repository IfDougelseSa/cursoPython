# Custo para cercar o terreno
c = float(input("Digite o comprimento do terreno: "))
l = float(input("Digite a largura do terreno: "))
preco_metro = float(input("Digite o preço da tela: "))

diametro = c + l
custo_total = diametro * preco_metro

print(f'O custo total para cercar seu terreno é {custo_total} reais.')

