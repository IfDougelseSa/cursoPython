# Soma dos algarimos de um numero inteiro maior do que zero
numero = int(input("Digite o numero inteiro: "))

soma = 0
while numero != 0:
    algarismo = numero % 10
    soma = soma + algarismo
    numero = numero // 10
print(soma)
