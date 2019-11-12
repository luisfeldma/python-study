dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().title()
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'       
for k, v in dados.items():
    print(f'{k} é igual a {v}.')
