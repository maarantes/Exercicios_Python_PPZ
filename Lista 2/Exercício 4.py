num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print ("O número" , num1 , "é maior!")
elif num2 > num1 and num2 > num3:
    print ("O número" , num2 , "é maior!")
elif num3 > num1 and num3 > num2:
    print ("O número" , num3 , "é maior!")
else:
    print ("Você precisa inserir 3 números distintos!")