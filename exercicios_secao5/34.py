# Notas e faltas de um aluno

faltas = int(input("Digite o número de faltas: "))
nota = float(input("Digite a nota: "))

if 9 <= nota <= 10:
    if faltas <= 20:
        print(f'A')
    else:
        print(f'B')
elif 7.5 <= nota < 9:
    if faltas <= 20:
        print(f'B')
    else:
        print(f'C')
elif 5 <= nota < 7.5:
    if faltas <= 20:
        print(f'C')
    else:
        print(f'D')
elif 4 <= nota < 5:
    if faltas <= 20:
        print(f'D')
    else:
        print(f'E')
elif 0 <= nota < 4:
    if faltas <= 20:
        print(f'E')
    else:
        print(f'E')
