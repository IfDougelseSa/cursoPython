# Numero entre 100 e 999 e os algarismo que compõem o mesmo!
lista = []
x = 1
while (x < 100) or (x > 999):
    x = int(input("Digite um numero: "))
n = x // 100
lista.append(n)
n = x % 100
z = n // 10
lista.append(z)
y = n % 10
lista.append(y)

print(f'O primeiro algarimo é {lista[0]}, o segundo {lista[1]} e o terceiro {lista[2]}.')


