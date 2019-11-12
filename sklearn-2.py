import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
#import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv(r"C:\Users\Felipe\Downloads\Real estate.csv")
# print(dataset.shape) #rows and collums
# print(dataset.describe()) 

# Plota o grafico do preco sobre o tempo
# dataset.plot(x='Date', y='Price', style='o')
# plt.title('PRICE VS DATE')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.show()

dataset.isnull().any()
dataset = dataset.fillna(method = 'ffill')

X = dataset[['X1 transaction date', 'X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores', 'X5 latitude', 'X6 longitude']].values
Y = dataset['Y house price of unit area'].values
plt.figure(figsize=(15,10))
plt.tight_layout()
sb.distplot(dataset['Y house price of unit area'])
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

regressor = LinearRegression().fit(X, Y)
regressor.score(X, Y)
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
print(coeff_df)

