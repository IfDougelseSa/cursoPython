# Data de nascimento válida

dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o ano do nascimento: "))
ano = int(input("Digite o mes do nascimento: "))



if mes == 1:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 2:
    if ano % 400 == 0:
        if dia <= 29:
            print(f'Essa data existe!')
        else:
            print(f'Essa data não existe!')
    elif ano % 4 == 0 and ano % 100 != 0:
        if dia <= 29:
            print(f'Essa data existe!')
        else:
            print((f'Essa data não existe'))
    else:
        if dia <= 28:
            print(f'Essa data existe!')
        else:
            print(f'Essa data não existe')
elif mes == 3:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 4:
    if dia <= 30:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 5:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 6:
    if dia <= 30:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 7:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 8:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 9:
    if dia <= 30:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 10:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 11:
    if dia <= 30:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')
elif mes == 12:
    if dia <= 31:
        print(f'Essa data existe!')
    else:
        print(f'Esse dia não existe nesse mês')

