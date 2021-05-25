# Empréstimo
salario = float(input("Digite seu sálario: "))
prestacao = float(input("Digite o valor da prestação: "))

if prestacao > (salario * 0.2):
    print(f'Empréstimo não concedido')
else:
    print(f'Empréstimo concedido')


