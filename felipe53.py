from datetime import date
hoje = date.today().year
dados = {'Nome': str(input('Nome: ')).strip().title(),
        'Idade': int(input('Ano de nascimento: ')),
        'CTPS': int(input('Carteira de Trabalho [0 não tem]: '))}
if dados['CTPS'] != 0:
    dados['Ano'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário: '))
    print(f'''{dados['Nome']}, você possui {hoje - dados['Idade']} anos e sua idade de aposentadoria é de {(dados['Ano'] - dados['Idade']) + 35}.''')        
else:
    print(f'ACABOU!')    