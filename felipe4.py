nome = str(input("Digite seu nome: ")).strip()
n = nome.split()
print(n)
print("Seu primeiro nome é: {}".format(n[0]))
print("Seu último nome é: {}".format(n[len(n) - 1]))

