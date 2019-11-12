t1 = int(input("Digite o primeiro termo de uma PA: "))
razão = int(input("Digite a razão dessa PA: "))

for c in range(t1, (t1 + (10 * razão)), razão):
    print(c, end=" -> ")
print("Acabou!")