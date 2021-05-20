# Soma dos quadrados de três numeros lidos

num1 = float(input('Digite o 1 numero: '))
num2 = float(input('Digite o 2 numero: '))
num3 = float(input('Digite o 3 numero: '))

soma = (num1 ** 2) + (num2 ** 2) + (num3 ** 2)
print(soma)


# Utilizando For
soma = 0

for values in range(3):
    values = float(input('Digite 3 numeros: '))
    quadrado = values ** 2
    soma = soma + quadrado
print(soma)

# Utilizando função
def soma_tres(num1=1, num2=2, num3=3):
    return (num1 ** 2) + (num2 ** 2) + (num3 ** 2)


print(soma_tres(2, 2, 2))



