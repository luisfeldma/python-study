frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = '' .join(palavras)
inverso = ''
print("Você digitou a frase: {}.".format(junto))
for letra in range((len(junto) - 1), -1, -1):
    inverso += junto[letra]
print("O inverso dessa frase eh :{}.".format(inverso))
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("Nao temos um palindromo")        