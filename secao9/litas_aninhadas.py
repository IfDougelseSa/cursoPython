"""
Listas aninhadas (Nested Lists)
- Algumas linguagens de programação (C/JAVA) possuem uma estrutura de dados chamadas de
arrays;
- Unidimensionais (arrays/vetores);
- Multidimensionais (Matrizes);


Em Python nós temos as Listas

numero = [1, 'b', 3.234, True, 5]

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][2]) # 3
print(listas[1][2]) # 6

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3



# Iterando com loops em uma lista aninhada
for lista in listas:
    print(lista)

for lista in listas:
    for values in lista:
        print(values)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# Outros Exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)


# Gerando valor inicias

print([['*' for i in range(1, 4)] for j in range(1,4)])
