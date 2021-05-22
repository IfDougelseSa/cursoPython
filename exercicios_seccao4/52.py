# Proporção em partes iguais
from fractions import gcd

premio = int(input("Digite o valor do prêmio: "))

apostador1 = int(input("Apostador 1, digite seu investimento: "))
apostador2 = int(input("Apostador 2, digite seu investimento: "))
apostador3 = int(input("Apostador 3, digite seu investimento: "))

mmc = gcd(apostador1, apostador2)
mmc_novo = gcd(mmc, apostador3)
proporcao = premio / mmc_novo

premio_apostador1 = apostador1 * proporcao
premio_apostador2 = apostador2 * proporcao
premio_apostador3 = apostador3 * proporcao


print(f'{premio_apostador1}\n{premio_apostador2}\n{premio_apostador3}')


"""
200

x + y + z = 200

x/4 + y/2 + z/5 = x+y+z/ 20


"""