preço = float(input("Digite o preço das compras: R$"))
print("""FORMAS DE PAGAMENTO:
[1] À VISTA DINHEIRO OU CHEQUE
[2] À VISTA NO CARTÃO
[3] PARCELADO EM 2 VEZES
[4] PARCELADO EM 3 VEZES OU MAIS""")
opção = int(input("Qual é a opção? "))
if opção == 1 :
    total1 = preço - (0.1 * preço)
    print("Seu desconto é de 10%. Você pagará {:.2f} R$.".format(total1))
elif opção == 2 :
    total2 = preço - (0.05 * preço)
    print("Seu desconto é de 5%. Você pagará {:.2f} R$.".format(total2))
elif opção == 3 :
    total3 = preço 
    print("Você pagará 2 parcelas de {:.2f}R$.".format(total3 / 2))
elif opção == 4 :
    total4 = preço + (0.2 * preço)
    x = int(input("Em quantas vezes você pretende pagar? "))
    print("Você pagará 20% de juros, sendo {} parcelas de {:.2f} R$.".format(x, (total4 /x)))
else : 
    print("Essa opção não está disponível. Escolha as opções de 1 a 4.")              