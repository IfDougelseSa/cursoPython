# Peso ideal
h = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

if sexo == "homem":
    peso_ideal = (72.7 * h) - 58
    print(peso_ideal)
else:
    peso_ideal = (62.1 * h) - 44.7
    print(peso_ideal)
