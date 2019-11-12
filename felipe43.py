lista = list()
resp = 's'
while resp not in 'Nn':
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
print(f'A lista completa é {lista}.')
lista_par = list()
lista_impar = list()
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)    
print(f'Os números pares são {lista_par}')
print(f'Os números ímpares são {lista_impar}')        


