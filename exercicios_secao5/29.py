# prova e números aleátorios para crianças
from random import randint


acertos = []
erros = []
tentativas = 0


while tentativas < 5:
    a = randint(0, 100)
    b = randint(0, 100)
    print(f'Qual é a soma de {a} + {b}?')
    tentativa = int(input("Digite a sua resposta: "))
    resposta = a + b
    if tentativa == resposta:
        print(f'Parabéns!!! Você acertou. A resposta é {resposta}')
        acertos.append(1)
    else:
        print(f'Tente novamente! A resposta é {resposta}')
        erros.append(1)
    tentativas = tentativas + 1


print(f'Você acertou {sum(acertos)} e errou {sum(erros)}')



