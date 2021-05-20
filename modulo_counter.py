"""
Módulo  Collections - Counter(Contador)

Collections -> High-performance Container datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passado como parâmetro e como valor a quantidade
de ocorrẽncias desse elemento.



# Utilizando o counter

from collections import Counter

#Exemplo 1

#Podemos utilizar qualquer iterável, aqui usamos uma lista.
lista = [1, 1, 2, 2, 3, 3, 3, 1 ,1 ,1 ,2 ,2 ,4 ,4 ,4 , 5, 5, 3 , 55, 33, 66 , 55, 44, 33, 22, 2, 22, 33]


res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 2: 5, 3: 4, 4: 3, 33: 3, 5: 2, 55: 2, 22: 2, 66: 1, 44: 1})

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade
# de ocorrências.

# Exemplo 2
print(Counter('Geek University'))
Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""


from collections import Counter

# Exemplo 3

texto = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

#Encontrado as 5 palavras com mais ocorrência no texto.
print(res.most_common(5))






