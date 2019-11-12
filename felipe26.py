print("----" * 15)
print("Este programa calcula a média de quantos valores você desejar.")
print("----" * 15)
soma = quant = 0
media = maior = menor = 0
resp = "S"
while resp in "S":
    n = float(input("Digite um número: "))
    resp = str(input("Deseja adicionar outro valor? [S/N] ")).upper().strip()[0]
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n        
print("A soma dos termos digitados é igual a {:.2f}, e a média é igual a {:.2f}.".format(soma, soma / quant)) 
print("O maior valor foi {} e o menor valor {}.".format(maior, menor))   
print("FIM.")    
