a1 = int(input("Digite o primeiro termo de uma PA: "))
razão = int(input("Digite a razão dessa PA: "))
c = -1
termo = a1
while c < 9:
    c += 1
    termo += razão
    print("{} >".format(termo, end = " "))
print("PAUSA")
mais = int(input("Quantos termos deseja mostrar a mais? "))


     


