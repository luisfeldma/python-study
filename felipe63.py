import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from time import sleep

style.use('ggplot')

#Indica o tempo que voce deseja pegar os dados
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

# --> Indica o dataframe, com nome, origem, comeco e fim
df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.tail())
# --> Transforma em csv e faz o download
#df.to_csv('tesla.csv')

#df = pd.read_csv('tesla.csv', parse_dates = True, index_col = 0)
#print(df.tail())

# --> Plotar o grafico; Aqui voce pode escolher qual coluna deseja ver
df.plot()

sleep(20)