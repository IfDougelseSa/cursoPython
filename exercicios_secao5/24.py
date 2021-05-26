# impostos sobre os estados

valor = float(input("Digite o valor: "))
estado = input("Digite o estado: ").upper()

if estado == "MG":
    total = valor * 1.07
    print(f'O preço final é {total}.')
elif estado == "SP":
    total = valor * 1.12
    print(f'O preço final é {total}.')
elif estado == "RJ":
    total = valor * 1.15
    print(f'O preço final é {total}.')
elif estado == "MS":
    total = valor * 1.08
    print(f'O preço final é {total}.')
else:
    print(f'Valor digitado está incorreto!')
    


