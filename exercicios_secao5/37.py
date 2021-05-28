# Tarifa de um estacionamento

#Colocar os valores
hora_chegada = int(input("Digite a hora da chegada: "))
minutos_chegada = int(input("Digite os minutos da chegada: "))
hora_saida = int(input("Digite a hora da saída: "))
minuto_saida = int(input("Digite os minutos da saída: "))


total_horas = hora_saida - hora_chegada
total_minutos = minuto_saida - minutos_chegada


if total_minutos < 0:
    hora_total = (total_horas * 60) + total_minutos
    print(hora_total)
    total_minutos = hora_total % 60
    total_horas =  hora_total // 60
    print(f'Você ficou {total_horas} horas e {total_minutos} minutos.')
else:
    print(f'Você ficou {total_horas} horas e {total_minutos} minutos.')


if total_horas == 0 and total_minutos > 0:
    valor_total = 1
    print(f'Você tem que pagar {valor_total} real.')
elif 1 <= total_horas <= 2:
    if total_horas == 1 and total_minutos == 0:
        valor_total = 1
        print(f'Você tem que pagar {valor_total} real.')
    elif total_horas == 2 and total_minutos == 0:
        valor_total = 2
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas == 0 and total_minutos > 0:
        valor_total = 1
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas == 1 and total_minutos > 0:
        valor_total = 2
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas == 2 and total_minutos > 0:
        valor_total = 3.40
        print(f'Você tem que pagar {valor_total} reais.')
elif 3 <= total_horas <= 4:
    if total_horas == 3 and total_minutos == 0:
        valor_total = 3.40
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas == 4 and total_minutos == 0:
        valor_total = 4.80
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas == 3 and total_minutos > 0:
        valor_total = 4.80
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas == 4 and total_minutos > 0:
        valor_total = 6.80
        print(f'Você tem que pagar {valor_total} reais.')
elif total_horas >= 5:
    if total_horas > 5 and total_minutos == 0:
        valor_total = 4.80 + (total_horas - 4) * 2
        print(f'Você tem que pagar {valor_total} reais.')
    elif total_horas > 5 and total_minutos > 0:
        valor_total = 4.80 + (total_horas - 4) * 2 + 2
        print(f'Você tem que pagar {valor_total} reais.')
























