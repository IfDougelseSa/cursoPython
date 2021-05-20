"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Quando uma função não retorna nenhum valor, o retorno é NONE.

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra
reservada return

OBS: Não precisamos necessariamente criar uma variavel para receber o retorno de uma função
Podemos passar a execução da função  para outras funções.

# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7*7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno: {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi '

alguem = "Pomba!"


print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a funcão, ou seja, ela sai da execução da função;
2 - Podemos ter em uma função diferentes returns;
3 - Podemos, em uma função retornar qualquer tipo de dado e até mesmo multiplos valores;


# Exemplos 1

def diz_oi():
    print('Estou sendo executadno antes do retorno')
    return 'Oi!'
    print('Estou senodo executado depois do return..')
print(diz_oi())

# Exemplo 2

def nova_funcao():
    variavel = x
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

#É POSSÍVEL IMPORTAR SUAS PROPRIAS FUNÇÕES


# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um numero pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara', valor
    return 'Coroa', valor
print(joga_moeda())
"""

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 4
    if numero % 2 != 0:
        return True
    return False
print(eh_impar())














