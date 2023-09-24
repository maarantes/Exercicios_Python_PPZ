peso = int(input("Digite o peso do seu peixe: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print ("Você atingiu o limite de 50 quilos com um excesso de" , excesso , "kg e deverá pagar R$" , multa , "de multa.")
else:
    excesso = 0
    multa = 0
    print ("Voce está dentro do limite. Há excesso de" , excesso , "kg e multa de R$" , multa)