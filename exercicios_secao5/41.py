# IMC de uma pessoa

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))


imc = peso / altura ** 2


if imc <= 18.5:
    print(f'Abaixo do peso')
    print(imc)
elif 18.6 <= imc <= 24.9:
    print(f'Saudável')
    print(imc)
elif 25 <= imc <= 29.9:
    print(f'Peso em excesso')
    print(imc)
elif 30 <= imc <= 34.9:
    print(f'Obesidade Grau 1')
    print(imc)
elif 35 <= imc <= 39.9:
    print(f'Obesidade Grau 2')
    print(imc)
elif imc >= 40:
    print(f'Obesidade Grau 3(mórbida)')
    print(imc)
