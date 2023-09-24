nota = int(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print ("Insira uma nota válida!")
    nota = int(input("Digite uma nota de 0 a 10: "))
else:
    print ("Nota registrada!")