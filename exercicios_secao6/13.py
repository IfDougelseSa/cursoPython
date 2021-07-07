# Número inteiro par em ordem crescente
n = 0
x = 1


while (x % 2) != 0:
    x = int(input("Digite um numero par: "))
while n <= x:
    print(n)
    n = n + 2


