texto = """The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.""".lower()

especial = [".", ",", ":", ]
lista_nova = []

for caracter in especial:
    texto = texto.replace(caracter, "")

for palavra in texto.split():
    if palavra[0] in "python" or palavra[-1] in "python":
        lista_nova.append(y)

print (lista_nova)