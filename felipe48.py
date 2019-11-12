matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
soma = soma3 = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for i in pares:
    soma += i
for c in range(0,3):
    soma3 += matriz[c][2]
for m in range(0,3):
    if m == 0:
        maior = matriz[1][m]
    if matriz[1][m] > maior:
            maior = matriz[1][m]     
print(f'A soma dos pares equivale a {soma}.')
print(f'A soma dos itens da 3a coluna é igual a {soma3}.')
print(f'O maior valor da segunda linha é {maior}.')