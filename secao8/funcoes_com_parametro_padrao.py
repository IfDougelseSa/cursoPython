"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(4))
print(quadrado()) # TypeError

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3)) # Por padrão eleva ao quadrado
print(exponencial(3, 5)) # Eleva a potência informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro numero,
# e sera calculado o quadrado deste número:
# Se o usuário passar dois argumentos, o primeiro será atríbuido ao parâmetro número
# e o segundo ao parâmetro potência, então será calculada essa potência.


# OBS: Em funções Python, os parâmetros com valores default (Padrão) DEVEM sempre
# estar ao final da declaração.

#ERRO!

def teste(num=2, potencia):
    return num ** potencia

print(teste(6))

# Correto

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=0, num2=0):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) #TypeError
print(soma()) #TypeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f"Olá {nome}"

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='Douglas'))
print(mostra_informacao('Sabrina'))

# Por quê utilizar parâmetros com valores default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Quaquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionarios, funções, etc;

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    return f'Oi {instrutor}' # Variável local

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável global
# a variável local terá preferência

def diz_oi():
    prof = "Geek" #Variável local
    return f'Ola {prof}!'

print(diz_oi()) #NameError

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 1

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento
    return total      # sem tem sido inicializada)

print(incrementa())

total = 0
def incrementa():
    global total # Avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de
# de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
"""













