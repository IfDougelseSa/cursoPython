# Soma dos n primeiros naturais
soma = 0
x = int(input("Digite um numero: "))


for numeros in range(x+1):
    soma = soma + numeros
print(soma)
