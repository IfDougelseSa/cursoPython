# Recebendo dois números
mult = 1
soma = 0


x = int(input("Digite o primeiro número: "))
y = int(input("Digite o secundo número: "))


if (x % 2) == 0:
    z = x + 1
    while x <= y:
        soma = soma + x
        x = x + 2
    while z <= y:
        mult = mult * z
        z = z + 2
elif (x % 2) != 0:
    z = x + 1
    while z <= y:
        soma = soma + z
        z = z + 2
    while x <= y:
        mult = mult * x
        x = x + 2


print(soma)
print(mult)
