# Dias da semana

x = int(input("Digite um numero entre 1 e 7: "))

if 1 <= x <=7:
    if x == 1:
        print("Domingo")
    elif x == 2:
        print("Segunda")
    elif x == 3:
        print("Terça")
    elif x == 4:
        print("Quarta")
    elif x == 5:
        print("Quinta")
    elif x == 6:
        print("Sexta")
    elif x == 7:
        print("Sábado")
else:
    print(f'Número inválido!')
