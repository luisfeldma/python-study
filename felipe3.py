nome = str(input("Digite seu nome: ")).strip()

print("Seu nome com letras maiusculas: ",nome.upper())
print("Seu nome com letras minusculas: ",nome.lower())
print("Seu nome possui {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome possui {} letras".format(len(nome.split()[0])))
