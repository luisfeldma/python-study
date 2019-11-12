galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper() 
        if pessoa['sexo'] in 'MF':
            break   
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
    if resp in 'N':
        break
média = soma / len(galera)        
print(galera)
print(f' - O grupo tem {len(galera)} pessoas.')
print(f' - A média de idade do grupo é {média}.')
print(f' - As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print(f'\n - Pessoas com idade acima da média: ', end='')        
for p in galera:
    if p['idade'] > média:
        print(f'{p["nome"]} ', end='')        
        
