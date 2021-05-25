# Número positivo ao quadrado e sua raiz

import math


x = float(input("Digite o numero: "))

if x >= 0:
    print(f'{x ** 2},{math.sqrt(x)}')
else:
    print("Número inválido!!")
