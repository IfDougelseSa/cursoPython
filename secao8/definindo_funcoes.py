"""
Definindo Funções
- Funções são pequenas partes de código que realizam  tarefas específicas;
- Pode ou não receber entrada de dddos e retornar uma saída de dados;
- Muito  uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos varias funções desde que iniciamos este curso:
- print()
-len()
-max()
-count()
e muitas outras;

# Exemplo de utilizaçao de funções


cores = ['amarelo', 'azul', 'verde', 'vermelho', 'preto', 'branco']


# Utilizando a função integrada (Built-in) do python print()


print(cores)

curso ='Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# curso.append('Mais dados') #AtributeError
# print(curso)

cores.clear()
print(cores)

# print(help(print))

# DRY - Dont Repeat Yoursef - Não repita você mesmo/ não repita seu código

# Mas então, como definir funções?



"""




"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parametro_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> Sempre com letras minusculas, e se for nome composto, separado por underline (Snake Case) 
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser
opcionais ou não;
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o processsamento da função
acontece
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos uma palavra reservada 'def' informando ao Python
que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos :
que é utilizado em Python para defirnir blocos.
"""

# Definição
def diz_oi():
    print('Oi!')
"""
OBS: 

1- Veja que dentro das nossas funções podemos utilizar outras funcões;
2- Veja que nossa função só executa 1 tarefa, a única coisa que ela faz é dizer oi;
3- Veja que esta função não recebe nenhum parãmetro de entrada;
4- Veja que esta função não retorna nada;
"""
# Utilizando funções

# Chamada de execução
# diz_oi()

"""
ATENÇÃO :

Nunca esqueça de utilizar o parenteses ao executar uma função.

Exemplo:

#Errado!
diz_oi
diz_oi ()

# Certo
diz_oi()
"""
# Exemplo 2

def cantar_parabens():
    print("Parabéns para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print("Viva o aniversariante!")

# cantar_parabens()


# for n in range(5):
  #  cantar_parabens()


# Em Python , podemos inclusive criar variáveis do tipo de uma função e executar esta função
#através da variável

canta = cantar_parabens
canta()


