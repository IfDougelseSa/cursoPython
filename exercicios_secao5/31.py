# Classificação da pessoa
h = float(input("Digite a altura: "))
p = float(input("Digite o peso: "))

if h < 1.20 and p < 60:
    print(f'A')
elif 1.20 <= h <= 1.70 and p < 60:
    print(f'B')
elif h > 1.70 and p < 60:
    print(f'C')
elif h < 1.20 and 60 <= p <= 90:
    print(f'D')
elif 1.20 <= h <= 1.70 and 60 <= p <= 90:
    print(f'E')
elif h > 1.70 and 60 <= p <= 90:
    print(f'F')
elif h < 1.20 and p > 90:
    print(f'G')
elif 1.20 <= h <= 1.70 and p > 90:
    print(f'H')
elif h > 1.70 and p > 90:
    print(f'I')

