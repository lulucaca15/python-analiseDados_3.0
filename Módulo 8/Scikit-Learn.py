import matplotlib.pyplot as plt
import numpy as np

Diametros = [[7], [10], [15], [30], [45]]
Precos = [[8], [11], [16], [38.5], [52]]

plt.figure()
plt.xlabel('Diâmetro(cm)')
plt.ylabel('Preço(R$)')
plt.title('Diâmetro x Preço')
plt.plot(Diametros, Precos, 'k.')
plt.axis([0, 60, 0, 60])
plt.grid(True)
plt.show()

from sklearn.linear_model import LinearRegression

X = [[7], [10], [15], [30], [45]]
Y = [[8], [11], [16], [38.5], [52]]

modelo = LinearRegression()

print(type(modelo))

modelo.fit(X, Y)
print("Uma pizza de 20cm de diâmetro deve custar: R$%.2f" %modelo.predict([20][0]))

from IPython.display import Image
Image('linear.png') 

print('Coeficiente: \n', modelo.coef_)
print("MSE: %.2f" %np.mean((modelo.predict(X) - Y) ** 2))
print('Score de Variação: %.2f' %modelo.score(X, Y))

plt.scatter(X, Y, color='black')
plt.plot(X, modelo.predict(X), color='blue', linewidth=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(())
plt.yticks(())

plt.show()
                    

