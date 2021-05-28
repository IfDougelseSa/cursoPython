# Aumento sálario

salario_atual = float(input("Digite o salário atual: "))
tempo_servico = int(input("Digite o numero de anos trabalhado: "))


if salario_atual <= 500 and tempo_servico < 1:
    novo_salario = salario_atual * 1.25
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual <= 500 and 1 <= tempo_servico <= 3:
    novo_salario = salario_atual * 1.25 + 100
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual <= 500 and 4 <= tempo_servico <= 6:
    novo_salario = salario_atual * 1.25 + 200
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual <= 500 and 7 <= tempo_servico <= 10:
    novo_salario = salario_atual * 1.25 + 300
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual <= 500 and tempo_servico > 10:
    novo_salario = salario_atual * 1.25 + 500
    print(f'Seu novo salário é: {novo_salario}')
elif 500 < salario_atual <= 1000 and tempo_servico < 1:
    novo_salario = salario_atual * 1.20
    print(f'Seu novo salário é: {novo_salario}')
elif 500 < salario_atual <= 1000 and 1 <= tempo_servico <= 3:
    novo_salario = salario_atual * 1.20 + 100
    print(f'Seu novo salário é: {novo_salario}')
elif 500 < salario_atual <= 1000 and 4 <= tempo_servico <= 6:
    novo_salario = salario_atual * 1.20 + 200
    print(f'Seu novo salário é: {novo_salario}')
elif 500 < salario_atual <= 1000 and 7 <= tempo_servico <= 10:
    novo_salario = salario_atual * 1.20 + 300
    print(f'Seu novo salário é: {novo_salario}')
elif 500 < salario_atual <= 1000 and tempo_servico >= 10:
    novo_salario = salario_atual * 1.20 + 500
    print(f'Seu novo salário é: {novo_salario}')
elif 1000 < salario_atual <= 1500 and tempo_servico < 1:
    novo_salario = salario_atual * 1.15
    print(f'Seu novo salário é: {novo_salario}')
elif 1000 < salario_atual <= 1500 and 1 <= tempo_servico <= 3:
    novo_salario = salario_atual * 1.15 + 100
    print(f'Seu novo salário é: {novo_salario}')
elif 1000 < salario_atual <= 1500 and 4 <= tempo_servico <= 6:
    novo_salario = salario_atual * 1.15 + 200
    print(f'Seu novo salário é: {novo_salario}')
elif 1000 < salario_atual <= 1500 and 7 <= tempo_servico <= 10:
    novo_salario = salario_atual * 1.15 + 300
    print(f'Seu novo salário é: {novo_salario}')
elif 1000 < salario_atual <= 1500 and tempo_servico > 10:
    novo_salario = salario_atual * 1.15 + 500
    print(f'Seu novo salário é: {novo_salario}')
elif 1500 < salario_atual <= 2000 and tempo_servico < 1:
    novo_salario = salario_atual * 1.10
    print(f'Seu novo salário é: {novo_salario}')
elif 1500 < salario_atual <= 2000 and 1 <= tempo_servico <= 3:
    novo_salario = salario_atual * 1.10 + 100
    print(f'Seu novo salário é: {novo_salario}')
elif 1500 < salario_atual <= 2000 and 4 <= tempo_servico <= 6:
    novo_salario = salario_atual * 1.10 + 200
    print(f'Seu novo salário é: {novo_salario}')
elif 1500 < salario_atual <= 2000 and 7 <= tempo_servico <= 10:
    novo_salario = salario_atual * 1.10 + 300
    print(f'Seu novo salário é: {novo_salario}')
elif 1500 < salario_atual <= 2000 and tempo_servico > 10:
    novo_salario = salario_atual * 1.10 + 500
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual > 2000 and tempo_servico < 1:
    novo_salario = salario_atual
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual > 2000 and 1 <= tempo_servico <= 3:
    novo_salario = salario_atual + 100
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual > 2000 and 4 <= tempo_servico <= 6:
    novo_salario = salario_atual + 200
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual > 2000 and 7 <= tempo_servico <= 10:
    novo_salario = salario_atual + 300
    print(f'Seu novo salário é: {novo_salario}')
elif salario_atual > 2000 and tempo_servico > 10:
    novo_salario = salario_atual + 500
    print(f'Seu novo salário é: {novo_salario}')

