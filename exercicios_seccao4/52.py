# Proporção em partes iguais
premio = int(input("Digite o valor do prêmio: "))

a = int(input("Apostador 1, digite seu investimento: "))
b = int(input("Apostador 2, digite seu investimento: "))
c = int(input("Apostador 3, digite seu investimento: "))


soma_investimento = a + b + c
proporcao = premio / soma_investimento
premio_apostador1 = proporcao * a
premio_apostador2 = proporcao * b
premio_apostador3 = proporcao * c


print(f'{premio_apostador1}\n{premio_apostador2}\n{premio_apostador3}')

