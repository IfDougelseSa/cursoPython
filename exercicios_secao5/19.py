# divisão por 3 e 5

x = int(input("Digite o numero: "))

if x % 3 == 0:
    print('Numero divisível por 3')
    if x % 5 == 0:
        print(f'Numero divisível por 5')
elif x % 5 == 0:
    print('Numero divisível por 5')
else:
    print('Não é divisível nem por 3 nem por 5')
