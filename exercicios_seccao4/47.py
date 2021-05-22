# Numero por linha

x = int(input("Digite o numero: "))

quarto_numero = x % 10
resto = x // 10
terceiro_numero = resto % 10
resto = resto // 10
segundo_numero = resto % 10
resto = resto // 10
primeiro_numero = resto % 10

print(f'{primeiro_numero}\n{segundo_numero}\n{terceiro_numero}\n{quarto_numero}')


