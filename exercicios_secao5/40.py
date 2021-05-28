# Custo de um carro ao consumidor

custo_fabrica = float(input("Digite o valor do custo de fabrica: "))


if custo_fabrica <= 12000:
    valor_total = custo_fabrica * 1.05
    print(valor_total)
elif 12000 < custo_fabrica <= 25000:
    valor_total = (custo_fabrica * 1.10) + custo_fabrica * 0.15
    print(valor_total)
elif custo_fabrica > 25000:
    valor_total = (custo_fabrica * 1.15) + custo_fabrica * 0.20
    print(valor_total)
    
