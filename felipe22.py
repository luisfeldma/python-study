v1 = float(input("Primeiro valor: "))
v2 = float (input("Segundo valor: "))
pergunta = 0
while pergunta < 5:
    print("""    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")
    pergunta = int(input(">>>>> Qual é sua opção? "))
    if pergunta == 4:
        print("Informe os novos valores: ")
        v1 = float(input("Primeiro valor: "))
        v2 = float(input("Segundo valor: "))
    elif pergunta == 3:
        if v1 > v2:
            print( "-" * 35)
            print("O primeiro valor é maior que o segundo.")
            print( "-" * 35)
        elif v1 == v2:
            print( "-" * 25)
            print("Os valores são iguais.")
            print( "-" * 25)
        else:
            print( "-" * 35)
            print("O segundo valor é maior que o primeiro.")
            print( "-" * 35)
    elif pergunta == 2:
        print( "-" * 40)
        print("Os números multiplicados equivalem a {}.".format(v1 * v2))
        print( "-" * 40)
    elif pergunta == 1:
        print( "-" * 40)
        print("A soma entre os números é igual a {}.".format(v1 + v2))                    
        print( "-" * 40)
print("Fim do programa.")
