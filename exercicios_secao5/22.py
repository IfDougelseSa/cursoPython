# aposentadoria

idade = int(input("Digite sua idade : "))
tempo_servico = int(input("Digite o tempo de serviço: "))

if idade > 65:
    print(f'Você já pode aposentar!!')
elif tempo_servico > 30:
    print(f'Você já pode aposentar!!')
elif tempo_servico > 25 and idade > 60:
    print(f'Você já pode aposentar!!')
else:
    print(f'Você não pode aposentar!!')
