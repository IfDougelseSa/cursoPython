# Consumo de um carro

distancia = float(input("Digite a distância: "))
litros = float(input("Digite a quantidade de litros: "))

total = distancia / litros

if total < 8:
    print(f'Venda o carro!')
elif 8 <= total <= 12:
    print(f'Econômico!')
else:
    print(f'Super econômico!')
