dados = []
nomes = []
maior = menor = 0
while True:
    nomes.append(str(input('Nome: ')).title().strip())
    nomes.append(int(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = nomes[1]
    elif nomes[1] > maior:
        maior = nomes[1]
    elif nomes[1] < menor:
        menor = nomes[1]        
    dados.append(nomes[:])
    nomes.clear()
    resp = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if resp in 'Nn':
        break   
print(f'No total, {len(dados)} pessoas foram cadastradas.')
print(f'O maior peso é de {maior} kgs, de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}.')
print(f'O menor peso é de {menor} kgs, de ', end='') 
for c in dados:
    if c[1] == menor:
        print(f'{p[0]}.')       




    