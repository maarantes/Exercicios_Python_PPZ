fuma_dia = int(input("Digite quantos cigarros você fuma por dia: "))
fuma_anos = int(input("Digite a quantos anos você fuma: "))

tempo_min = fuma_dia*10*fuma_anos*365
tempo_dias = tempo_min/1440

print (f"Você já perdeu {tempo_dias:.2f} dias de vida.")