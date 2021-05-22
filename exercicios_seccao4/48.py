# Segundos para horas, minutos e segundos

segundos = int(input("digite os segundos:"))

hora = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{hora} horas, {minutos}minutos e {segundos}segundos')




"""
1hora tem 3600 segundos
1min tem 60 segundos
"""