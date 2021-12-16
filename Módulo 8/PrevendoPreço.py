from os import terminal_size
from re import S
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston
boston = load_boston()

# print(type(boston))
# print(boston.data.shape)
# print(boston.DESCR)
# print(boston.feature_names)

df = pd.DataFrame(boston.data)
# print(df.head())

df.columns = boston.feature_names
# print(df.head())

# print(boston.target)

df['PRICE'] = boston.target
# print(df.head()) 

from sklearn.linear_model import LinearRegression  

X = df.drop('PRICE', axis=1)
Y = df.PRICE

# plt.scatter(df.RM, Y)
# plt.xlabel('Média do Número de Quartos por Casa')
# plt.ylabel('Preço da Casa')
# plt.title('Relação entre Número de Quartos e Preço')
# plt.show()

regr = LinearRegression()
# print(type(regr))
regr.fit(X, Y)
print('Coeficientes: ', regr.intercept_)
print('Número de Coeficientes', len(regr.coef_))

# print(regr.predict(X))

# plt.scatter(df.PRICE, regr.predict(X))
# plt.xlabel('Preço Original')
# plt.ylabel('Preço Previsto')
# plt.title('Preço Original x Preço Previsto')
# plt.show()

# mse1 = np.mean((df.PRICE - regr.predict(X)) ** 2)
# print(mse1)

# regr = LinearRegression()
# regr.fit(X[['PTRATIO']], df.PRICE)
# mse2 = np.mean((df.PRICE - regr.predict(X[['PTRATIO']])) ** 2)
# print(mse2)

X_treino = X[:-50]
X_teste = X[-50:]

Y_treino = X[:-50]
Y_teste = X[-50:]

print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)

from sklearn.model_selection import train_test_split

X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, df.PRICE, test_size = 0.30, random_state=5)
print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)

regr = LinearRegression()
regr.fit(X_treino, Y_treino)

pred_treino = regr.predict(X_treino)
pred_teste = regr.predict(X_teste)

plt.scatter(regr.predict(X_treino), regr.predict(X_treino) - Y_treino, c='b', s=40, alpha=0.5)
plt.scatter(regr.predict(X_teste), regr.predict(X_teste) - Y_teste, c='g', s=40, alpha=0.5)
plt.hlines(y=0, xmin=0, xmax=0)
plt.ylabel('Residuo')
plt.title('Residual Plot - Treino(Azul), Teste(Verde)')
plt.show()