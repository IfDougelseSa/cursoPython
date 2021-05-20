# Média aritmética
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)

# Utilizando For

soma = 0

for values in range(4):
    values = float(input('Digite a nota: '))
    soma = soma + values

media = soma / 4
print(media)

