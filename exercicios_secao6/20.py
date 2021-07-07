#Sequência de pares ou não e sua contagem
x = None
par = 0
impar = 0
pares = []


print(f'Digite 1000 para sair!')
while x != 1000:
    x = int(input("Digite um numero: "))
    if (x % 2) == 0:
        pares.append(x)
        par = par + 1
    else:
        impar = impar + 1


pares.pop()
total_par = par - 1
total = total_par + impar


print(f'O número de dados lidos {total}. \n'
      f'O número de números pares digitados {total_par}.\n'
      f'Os números pares digitados: {pares}.')


