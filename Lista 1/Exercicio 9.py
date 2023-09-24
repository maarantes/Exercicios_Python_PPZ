dist_percorrida = int(input("Digite a distância percorrida em km: "))
quant_dias = int(input("Digite a quantidade de dias alugados: "))
preco = dist_percorrida*0.15 + quant_dias*60
print (f"O preço total é: R$ {preco:.2f}")