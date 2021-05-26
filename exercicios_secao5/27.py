# idade nadador

idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    print(f'Infantil A')
elif 8 <= idade <= 10:
    print(f'Infantil B')
elif 11 <= idade <= 13:
    print(f'Juvenil A')
elif 14 <= idade <= 17:
    print(f'Juvenil B')
else:
    print(f'Sênior')
