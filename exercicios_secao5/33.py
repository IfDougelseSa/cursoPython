# Preço antigo e novo de um produto

preco_antigo = float(input("Digite o preço antigo: "))

if preco_antigo < 50:
    preco_novo = preco_antigo * 1.05
elif 50 <= preco_antigo <= 100:
    preco_novo = preco_antigo * 1.10
else:
    preco_novo =  preco_antigo * 1.15


if preco_novo <= 80:
    print(f'Barato\n{preco_novo}')
elif 80 < preco_novo <= 120:
    print((f'Normal\n{preco_novo}'))
elif 120 < preco_novo <= 200:
    print((f'caro\n{preco_novo}'))
else:
    print(f'Muito caro\n{preco_novo}')

