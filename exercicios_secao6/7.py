# Média de 10 inteiros

soma = 0
cont = 0
for values in range(10):
    num = int(input("Digite o numero: "))
    if num > 0:
        soma = soma + num
        cont = cont + 1
        media = soma / cont
    elif num < 0:
        continue

print(f'A média é {media}')

