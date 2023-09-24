num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

erro = 0

if num1  == num2 or num1 == num3 or num2 == num3:
    print ("Você precisa inserir 3 números distintos!")
    erro = 1
elif num1 > num2 and num2 > num3:
    print ("O número" , num1 , "é o maior!")
elif num2 > num1 and num2 > num3:
    print ("O número" , num2 , "é o maior!")
else:
    print ("O número" , num3 , "é o maior!")


if erro == 0:
    if num1 < num2 and num1 < num3:
        print ("O número" , num1 , "é o menor!")
    elif num2 < num1 and num2 < num3:
        print ("O número" , num2 , "é o menor!")
    else:
        print ("O número" , num3 , "é 0 menor!")

        