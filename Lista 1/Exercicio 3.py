dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos "))

dias_convertido = dias*86400
horas_convertido = horas*3600
minutos_convertido = minutos*60

total_tempo = dias_convertido + horas_convertido + minutos_convertido

print ("Conversão desse tempo em segundos:" , total_tempo)