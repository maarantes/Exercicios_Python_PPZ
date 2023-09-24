lado1 = int(input("Digite o tamanho do primeiro lado: "))
lado2 = int(input("Digite o tamanho do segundo lado: "))
lado3 = int(input("Digite o tamanho do terceiro lado: "))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print ("Não é possível formar um triângulo com esses valores!")
elif lado1 == lado2 == lado3:
    print ("Esse triângulo é equilátero!")
elif lado1 != lado2 != lado3:
    print ("Esse triângulo é escaleno!")
else:
    print ("Esse triângulo é isósceles!")