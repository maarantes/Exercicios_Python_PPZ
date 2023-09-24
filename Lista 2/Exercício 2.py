from calendar import isleap

ano = int(input("Digite o ano: "))

if isleap(ano):
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")
