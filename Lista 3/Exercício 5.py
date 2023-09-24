num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num1 % num2 != 0:
   num1, num2 = num2, num1 % num2

print (num2)