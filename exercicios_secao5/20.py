# determinando um triângulo

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b and a == c:
        print(f'Triângulo equilátero')
    elif a == b or a == c or b == c:
        print(f'Triângulo isósceles')
    else:
        print(f'Triângulo escaleno')
else:
    print(f'Não é possível formar um triângulo com essas medidas!')

