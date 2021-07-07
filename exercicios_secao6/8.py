# Menos valor lido / Maior valor lido

menor = 0
maior = 0

for values in range(10):
    num = int(input("Digite o valor: "))
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
print(f'o maior numero é {maior} e o menor é {menor}.')






