import random

lista = random.sample(range(100), 20)

par = []
impar = []

for x in lista:
    if x % 2 == 0:
        par.append (x)
    else:
        impar.append (x)

print ("Lista:" , lista)
print ("Números pares:" , par)
print ("Números impares:" , impar)