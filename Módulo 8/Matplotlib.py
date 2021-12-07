import matplotlib as mpl
import matplotlib.pyplot as plt

print(mpl.__version__)

# plt.plot([1,3,5], [2,5,7])
# plt.show()

x = [1,4,5]
y = [3,7,2]

# plt.plot(x, y)
# plt.xlabel('Variável 1')
# plt.ylabel('Variável 2')
# plt.title('Teste Plot')
# plt.show()

x2 = [1,2,3]
y2 = [11,12,15]

# plt.plot(x2, y2, label = 'Primeira Linha')
# plt.legend()
# plt.show()

x = [2,4,6,8,10]
y = [6,7,8,2,4]

plt.bar(x, y, label = 'Barras', color='r')
plt.legend()
plt.show()