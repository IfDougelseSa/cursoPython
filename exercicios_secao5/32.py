# Produto do cardápio

produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

if produto == 100:
    print(f'Você escolheu {quantidade} Cachorro Quente!')
    total = 1.20 * quantidade
    print(f'O valor total é {total}.')
elif produto == 101:
    print(f'Você escolheu {quantidade} Bauru(s) Simples!')
    total = 1.30 * quantidade
    print(f'O valor total é {total}')
elif produto == 102:
    print(f'Você escolheu {quantidade} Bauru(s) Ovo(s)!')
    total = 1.50 * quantidade
    print(f'O valor total é {total}')
elif produto == 103:
    print(f'Você escolheu {quantidade} Hambuguer(s)!')
    total = 1.20 * quantidade
    print(f'O valor total é {total}')
elif produto == 104:
    print(f'Você escolheu {quantidade} Cheeseburguer(s)!')
    total = 1.70 * quantidade
    print(f'O valor total é {total}')
elif produto == 105:
    print(f'Você escolheu {quantidade} Suco(s)!')
    total = 2.20 * quantidade
    print(f'O valor total é {total}')
elif produto == 106:
    print(f'Você escolheu {quantidade} Refrigerante(s)!')
    total = 1.00 * quantidade
    print(f'O valor total é {total}')
