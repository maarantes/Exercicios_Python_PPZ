import math

tamanho = int(input("Digite o tamanho, em metros quadrados, da área a ser pintada: "))
lata = tamanho / 54
comprar_lata = math.ceil(lata)
comprar_preco = comprar_lata * 80
print ("Você precisa comprar" , comprar_lata , "latas de tinta, o que irá custar R$" , comprar_preco)