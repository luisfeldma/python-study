listagem = ('Lápis', 1.50, 'Borracha', 6.00, 'Caderno', 12.00, 'Estojo', 16.50, 'Lapiseira', 17.50)
print('--' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--' * 20)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R$ {listagem[item]:>6.2f}')