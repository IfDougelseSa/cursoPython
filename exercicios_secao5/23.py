# ano bissexto

ano = int(input("Digite o ano: "))

if (ano % 400) == 0:
    print(f'Ano bissexto.')
elif (ano % 4 == 0) and (ano % 100) != 0:
    print(f'Ano bissexto.')
else:
    print(f'O ano digitado não é bissexto.')

