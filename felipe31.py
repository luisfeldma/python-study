print("-------LOJA DE ELETRÔNICOS-------")
total = mais_de_mil = cont = menor = 0
mais_barato = " "
while True:
    nome = str(input("Digite o nome do produto: ")).strip().title()
    preço = float(input("Digite o preço do produto: R$ "))
    resp = str(input("QUER CONTINUAR? [S/N] ")).strip().upper()[0]
    total += preço
    cont += 1
    if cont == 1:
        mais_barato = nome
        menor = preço
    elif nome < mais_barato:
        mais_barato = nome
        menor = preço    
    if preço > 1000:
        mais_de_mil +=1
    while resp not in "SN":
        resp = str(input("QUER CONTINUAR?[S/N] ")).strip().upper()[0]
    if resp in "N":
        print("---------FIM DO PROGRAMA---------")
        break
print("O total da compra foi de {:.2f} R$.".format(total))
print(f"{mais_de_mil} produtos custam mais de 1.000 R$.")
print(f"O produto mais barato é {mais_barato} e custou {menor} R$.")
