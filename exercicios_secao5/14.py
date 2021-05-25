# Média ponderada
nota_laboratorio = float(input("Digite a nota do laboratório: "))
nota_semestral = float(input("Digite a nota semestral: "))
nota_final = float(input("Digite a nota final: "))


media = ((nota_laboratorio * 2) + (nota_semestral * 3) + (nota_final * 5)) / 10


if (0 <= nota_laboratorio <= 10) and (0 <= nota_semestral <= 10) and (0 <= nota_final <= 10):
    if 0 <= media <= 2.9:
        print(f'Aluno reprovado!')
        print(media)
    elif 2.9 < media <= 4.9:
        print(f'Aluno de exame!')
        print(media)
    else:
        print(f'Aluno aprovado!')
        print(media)
else:
    print(f'Foi digitado uma nota inválida.')

