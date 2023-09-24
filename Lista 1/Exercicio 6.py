distancia = int(input("Digite a distância (km) até o destino: "))
vel_media = int(input("Digite a velocidade média (km/h) em que você dirigirá: "))
tempo = distancia/vel_media
print (f"A viagem durará {tempo:.2f}" , "horas.")