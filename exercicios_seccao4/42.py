# Salário

salario = float(input('Digite o salário: '))

gratificacao = salario * 0.05
imposto = salario * 0.07
total = (salario + gratificacao) - imposto

print(f'O seu salário é {total}.')
