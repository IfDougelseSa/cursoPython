# Logaritmo de um numero positivo.
import math

x = float(input("Digite o numero: "))

if x < 0:
    print("Número inválido")
else:
    print(math.log(x, 10))
