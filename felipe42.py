lista = list()
resp = 's'
while resp not in 'Nn':
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
print(f'A lista possui esses valores: {lista}')    
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista em ordem reversa é {lista}')
if 5 in lista:
    print('O 5 está na lista.')
else:
    print('O 5 não está na lista.')    
  

