n = int(input("Digite um número inteiro [menor que 999]: "))
cont = 0
soma = 0
while n < 999:
    cont += 1
    soma += n
    n = int(input("Digite um número inteiro: "))
print("A soma é igual a {}.".format(soma))    
print("Você digitou {} números.".format(cont))
print("FIM.")