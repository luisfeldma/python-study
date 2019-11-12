print("Digite seu peso e altura para calcular seu IMC: ")

peso = float(input("Digite seu peso (em kilogramas): "))
altura = float(input("Digite sua altura (em metros): "))
imc = peso / (altura * 2)

print("Calculando...")

print("Seu IMC é {:.1f}.".format(imc))

if imc <= 18.5 :
    print("ABAIXO DO PESO.")
elif 18.5 < imc <= 25 :
    print("PESO IDEAL.")
elif 25 < imc <= 30 :
    print("SOBREPESO.")
elif 30 < imc <= 40 :
    print("OBESIDADE.")
else :
    print("OBESIDADE MÓRBIDA.")

