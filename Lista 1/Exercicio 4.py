salario = int(input("Digite o salário: "))
aumento = int(input("Digite a porcentagem do aumento: "))
salario_novo = salario + salario * aumento/100
print (f"Seu salário novo: R$ {salario_novo:.2f}")
