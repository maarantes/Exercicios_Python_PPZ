ganha_hora = float(input("Digite o quanto você ganha por hora: "))
horas_mes = float(input("Digite quantas horas você trabalha por mês: "))

salario_bruto = ganha_hora * horas_mes
imposto = salario_bruto * 11/100
previdencia = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
salario_liquido = salario_bruto - imposto - previdencia - sindicato

print (f"Segue a lista dos descontos de seu salário:")
print (f"Salário bruto: R${salario_bruto:.0f}")
print (f"Imposto de Renda: -R${imposto:.0f}")
print (f"Previdência: -R${previdencia:.0f}")
print (f"Sindicato: -R${sindicato:.0f}")
print (f"Salário Líquido: R$ {salario_liquido:.0f}")
