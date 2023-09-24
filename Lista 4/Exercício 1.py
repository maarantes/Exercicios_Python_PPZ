import random

lista = random.sample(range(100), 10)

maior = menor = lista[0]

for x in lista:
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print ("Lista:" , lista)
print ("Maior número:" , maior)
print ("Menor número:" , menor)