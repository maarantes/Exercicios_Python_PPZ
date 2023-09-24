preco = int(input("Digite o preço da mercadoria: "))
desconto = int(input("Digite a porcentagem do desconto: "))
novo_preco = preco - preco * desconto/100
print (f"A mercadoria com esse desconto custa: R$ {novo_preco:.2f}")
