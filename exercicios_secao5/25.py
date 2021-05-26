# Raízes da equação de 2 grau
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


if a != 0:
    delta = (b ** 2 - 4 * a * c)
    if delta >= 0:
        print(f'Duas raízes')
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(x1)
        print(x2)
    elif delta == 0:
        print(f'Raiz única')
        x = -b / (2 * a)
        print(x)
    else:
        print(f'A equação não possui raízes reais.')
else:
    print(f'Não é equação do segundo grau.')

