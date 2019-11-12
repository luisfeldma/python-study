from time import sleep
import pandas as pd

base_dados = list()
cliente = dict()
n_atual = 0
listdict = list()

#Cadastro dos clientes na base de dados
while True:
    
    cliente.clear()
    cliente['Nome'] = str(input('Digite o nome do Cliente: ')).strip().title() 
    cliente['Agencia'] = str(input('Digite o numero da agencia: ')).strip().title()
    cliente['Conta Corrente'] = str(input('Digite o numero da conta corrente: ')).strip().title()
    base_dados.append(cliente.copy())
    pergunta = str(input('Deseja continuar cadastrando clientes? [S/N] ')).upper().strip()

    if len(cliente['Nome']) > 30 or len(cliente['Agencia']) != 5 or len(cliente['Conta Corrente']) != 7:
        print("Dados invalidos. Verifique as condicoes.")
        base_dados[n_atual].clear()

    if 'N' in pergunta:
        break
    n_atual += 1

tabela = pd.DataFrame(base_dados)
print(tabela)


sleep(7)










