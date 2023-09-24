nome = str(input("Digite seu nome de usuário: "))
senha = str(input("Digite sua senha: "))

while nome == senha:
    print ("Erro! O nome de usuário não pode ser o mesmo que a senha!")
    nome = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))
else:
    print ("Bem vindo, usuário" , nome)