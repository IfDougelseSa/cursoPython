# Média de 10 inteiros

soma = 0
for values in range(10):
    num = int(input("Digite o numero: "))
    soma = soma + num

media = soma / 10
print(f'A média é {media}')
