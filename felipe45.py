pessoas = []
lista = []
maiores = menores = 0
for p in range(0,3):
    lista.append(str(input('Nome: ')).strip().title())
    lista.append(int(input('Idade: ')))
    pessoas.append(lista[:])
    lista.clear()
for c in pessoas:
    if c[1] >= 18:
        maiores += 1
        print(f'{c[0]} é maior de idade.')
    else:
        menores += 1
        print(f'{c[0]} é menor de idade.')
print(f'Temos {menores} menores de idade e {maiores} maiores de idade.')            
