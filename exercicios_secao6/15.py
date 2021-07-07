#ímpares em ordem crescente
x = 0

while (x % 2) == 0:
    x = int(input("Digite um numero ímpar: "))
for numeros in range(1, x+1, 2):
    print(numeros)

