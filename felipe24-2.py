print("-"*25)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*25)

n1 = 0
n2 = 1
cont = 2      # 0 1 1 2 3 5 8 13 21 34 55
quest = int(input("Quantos termos você deseja mostrar? "))

print(f"{n1} > {n2}", end="")

while True:
    
    n3 = (n1 + n2)
    print(f" > {n3}", end="")
    n1 = n2
    n2 = n3
    cont += 1
    if cont >= quest:
        break

print(" > FIM")    