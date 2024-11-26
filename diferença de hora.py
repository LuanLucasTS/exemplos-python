from datetime import datetime, timedelta

data_inicio = datetime.now()

duracao = '2:00:00' #input('Quanto tempo durara o experimento (formato Horas:Minutos:Segundos): ')
horas, minutos, segundos = map(int, duracao.split(':'))
# transforma a string em timedelta
duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)
# soma a data à duração
termino = data_inicio + duracao
# formata o resultado
print(termino.strftime('%H:%M:%S'))



horabd = '15:15:25'
horas, minutos, segundos = map(int, horabd.split(':'))
horabd = timedelta(hours=horas, minutes=minutos, seconds=segundos)

data_inicio = datetime.now().strftime('%H:%M:%S')
data_inicio = str(data_inicio)
horas, minutos, segundos = map(int, data_inicio.split(':'))
data_inicio = timedelta(hours=horas, minutes=minutos, seconds=segundos)

expira = horabd - data_inicio

print(expira)

if expira < timedelta(hours=0, minutes=0, seconds=0):
    print('token expirado')
else:
    print('token valido')





'''
horabanco = '18:23:00'
then = datetime.strptime(f'{horabanco}',"%H:%M:%S")
now = datetime.now()

print(then)
print(now)


diferenca = then - now
print(diferenca)
'''

