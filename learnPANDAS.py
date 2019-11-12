import pandas as pd 
import matplotlib.pyplot as plt

data = {'Luis Felipe': [7, 8, 5, 10], 'Pedro Nirschl': [10, 9, 6, 7]} #Dictionary

# Mostra a tabela com as notas. Keys viram colunas e os Values linhas
tabela = pd.DataFrame(data)
print(tabela)

# Mostra as informacoes dos dados
print(tabela.info())

# .shape mostra uma tupla de (linhas, colunas)
print(tabela.shape)

# .columns mostra o nome das colunas
print(tabela.columns)

# .rename() renomeia a coluna que voce quiser
tabela.rename(columns={'Pedro Nirschl': 'Matheus Hirata'}, inplace=True)
print(tabela.columns)

# Deixa todas as letras em minusculo
tabela.columns = [col.lower() for col in tabela]
print(tabela.columns)

# .isnull() Verifica quais dados sao 'nulos'
print(tabela.isnull())
print(tabela.isnull().sum())

# .dropna() Remove linhas com valores nulos
tabela.dropna()
print(tabela)

# .dropna(axis=1) remove as colunas com valores nulos
tabela.dropna(axis=1)
print(tabela)

# .describe() Mostra todos os detalhes do df, (count, mean, min, max etc)
print(tabela.describe())

# .corr() mostra a tabela de correlacao entre os dados da coluna
print(tabela.corr())

# Puxa apenas os valores das colunas selecionadas do df
coluna_lf = tabela['luis felipe']
print(coluna_lf.head())

# Para adicionar colunas específicas é só adicionar os nomes das que você deseja selecionar
coluna_lfmh = tabela[['luis felipe', 'matheus hirata']]
print(coluna_lfmh.head())
