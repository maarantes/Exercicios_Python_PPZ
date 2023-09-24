num = int(input("Digite o número: "))
primeiro, segundo = 1, 1
contador = 1

while contador <= num - 2:
    primeiro, segundo = segundo, primeiro + segundo
    contador = contador + 1
print ("O número de Fibonacci do número" , num , "é" , segundo)