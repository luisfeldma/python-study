from random import randint
ns = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os numeros sorteados foram: ')
for n in ns:
    print(f'{n} ', end = '')
print(f'\nO maior valor foi {max(ns)}.')
print(f'O menor valor foi {min(ns)}.')
