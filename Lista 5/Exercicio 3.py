contador = 0

for x in range (1067, 3628):
    if x % 2 == 0 and x % 7 == 0:
        contador = contador + 1

print (contador)