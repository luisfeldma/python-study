valores = list()
maior = menor = 0
for x in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if x == 0:
        maior = menor = valores[x]
    else:
        if valores[x] > maior:
            maior = valores[x]
        elif valores[x] < menor:
            menor = valores[x]
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior}, que esta na posicao ', end = '')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}...', end = '')
print(f'\nO menor valor foi {menor}, que esta na posicao ', end = '') 
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end = '')                            
   