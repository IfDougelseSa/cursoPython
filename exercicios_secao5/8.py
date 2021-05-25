# média com notas válidas
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

if (0 <= nota1 <= 10) and (0 <= nota2 <= 10):
    media = (nota1 + nota2) / 2
    print(f'A sua média é {media}.')
else:
    print(f'Valor da nota inválido.')

