n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
f = float(input("Sua frequência: "))
m = (n1 + n2)/2

print("Sua média final é: {}!".format(m))

if f >= 0.7:
    if m >= 5.0:
        print("Aprovado!")
    else:
        print("Reprovado por nota!")    
else:
    if m < 5:
        print("Reprovado por nota e faltas!")
    else:
        print("Reprovado por faltas!")


    
    
