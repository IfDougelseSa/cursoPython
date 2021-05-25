# Média ponderada com aprovação
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


if (0 <= nota1 <= 100) and (0 <= nota2 <= 100) and (0 <= nota3 <= 100):
    media = (nota1 * 1) + (nota2 * 1) + (nota3 * 2) / 4
    if media >= 125:
        print(f'Aprovado!!')
        print(media)
    else:
        print(f'Reprovado!!')
        print(media)
else:
    print("Nota inválida!!")





