# Digitos invertidos
num = int(input('Digite o numero com 3 digitos: '))

primeiro_numero = num % 10
resto = num // 10
segundo_numero = resto % 10
resto = resto //10
terceiro_numero = resto % 10

print(f'{primeiro_numero}{segundo_numero}{terceiro_numero}')









