lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor armazenado com sucesso...')
    else:
        print('Valor duplicado... Nao vou adicionar.')    
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta in 'Nn':
        break
print(lista)