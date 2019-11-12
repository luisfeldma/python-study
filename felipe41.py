lista = list()
for c in range(0,5):
    n = (int(input('Digite um valor: ')))
    if c == 0:
        lista.append(n)
        print('Adicionado a lista...')
    elif n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while True:
            if n < lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista.')
                break
            pos += 1


print(lista)


