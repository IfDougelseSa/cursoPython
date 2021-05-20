"""
Funções que recebem dados para serem processados dentro da mesma;

Se e gente pensar em um programa, geralmente temos:

entrada ->  processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(3))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) #TypeError
 def cantar_parabens(aniversariante):
    print("Parabéns para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva o {aniversariante}!")

cantar_parabens("Douglas")

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 4))

print(multiplica(2, 5))

print(outra(2, 4, "\tola"))

# OBS: Se a gente informar um numero errado de parâmetros ou argumentos, teremos TypeError.

# print(soma(2, 3, 4)) #TypeError - Passando argumentos a mais
# print(soma(4)) #TypeError - Passando argumentos a menos

# Nomeando parâmetros

def nome_completo(primeiro_nome, sobrenome):
    return f'O seu nome completo {primeiro_nome} {sobrenome}.'


print(nome_completo('Douglas', 'Cortez'))

# A diferença entre parâmetros e argumentos

# Parâmetros são variáveis declaradas na definição de uma funcão;
# Argumentos são dados passados durante a execução de uma função;


# A ordem dos parâmetros importa!

primeiro_nome = "Felicity"
sobrenome = "Jones"

print(nome_completo(sobrenome, primeiro_nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(primeiro_nome="Douglas", sobrenome="Cortez"))
print(nome_completo(sobrenome="Cortez", primeiro_nome="Douglas"))
"""
# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

list = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(list))

# A função recebe qualquer tipo de parâmetro













