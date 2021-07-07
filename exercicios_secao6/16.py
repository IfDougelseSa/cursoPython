# Números ímpares de ordem decrescente
x = 0

while (x % 2) == 0:
    x = int(input("Digite um numero ímpar: "))
for numeros in range(x, 0, -2):
    print(numeros)

