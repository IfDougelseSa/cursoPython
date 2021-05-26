# médias
import math

x = int(input("Digite o valor 1, 2, 3 ou 4: "))


if x == 1:
    print(f'Você escolheu média geométrica!')
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    media = (a * b * c) ** (1/3)
    print(media)
elif x == 2:
    print(f'Você escolheu média ponderada!')
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    media = (a + (2 * b) + (3 * c)) / 6
    print(media)
elif x == 3:
    print(f'Você escolheu média harmônica!')
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    media = 1 / ((1 / a) + (1 / b) + (1 / c))
    print(media)
elif x == 4:
    print(f'Você escolheu média aritmética!')
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    media = (a + b + c) / 3
    print(media)

