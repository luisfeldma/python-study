print(" ")
print("Para analisar as condições do empréstimo, digite as informações pedidas: ")
print(" ")
valor = float(input("Digite o valor da casa: "))
sal = float(input("Digite o valor do seu salário (mensal): "))
tempo_an = int(input("Digite o tempo (em anos) que você pretende pagar o valor da casa: "))
tempo_men = tempo_an * 12
prestação = valor / tempo_men
print(" ")
print("Analisando condições para a concessão...")
print(" ")
if prestação >= 0.3 * sal :
    print("Não será possível realizar seu empréstimo... O valor da prestação excede 30% do seu salário.")
else :
    print("Seu empréstimo será concedido, e o valor das parcelas mensais será de {:.2f} reais.".format(prestação))
print(" ")

