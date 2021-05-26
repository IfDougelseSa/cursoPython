# Operações matemáticas

x = int(input("Digite o valor 1 para adição, 2 para subtração, 3 para mutiplicaçaõ e 4 para divisão: "))

if x == 1:
    print(f'Você escolheu adição!')
    a = int(input("Digite o numero 1: "))
    b = int(input("Digite o numero 2: "))
    conta = a + b
    print(f'O valor da conta é {conta}.')
elif x == 2:
    print(f'Você escolheu subtração!')
    a = int(input("Digite o numero 1: "))
    b = int(input("Digite o numero 2: "))
    if a > b:
        conta = a - b
        print(f'O valor da conta é {conta}.')
    else:
        conta = b - a
        print(f'O valor da conta é {conta}.')
elif x == 3:
    print(f'Você escolheu mutiplicação!')
    a = int(input("Digite o numero 1: "))
    b = int(input("Digite o numero 2: "))
    conta = a * b
    print(f'O valor da conta é {conta}.')
elif x ==  4:
    print(f'Você escolheu divisão!')
    a = int(input("Digite o numero 1: "))
    b = int(input("Digite o numero 2: "))
    if b == 0:
        print(f'O denominador não pode ser zero')
    else:
        conta = a / b
        print(f'O valor da conta é {conta}.')

