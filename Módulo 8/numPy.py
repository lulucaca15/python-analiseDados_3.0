import numpy as np

print(np.__version__)

print(help(np.array))

vetor1 = np.array([0,1,2,3,4,5,6,7,8])
print(vetor1)
print(type(vetor1))

print(vetor1.cumsum())

lst = [0,1,2,3,4,5,6,7,8]
print(lst)

print(type(lst))

print(vetor1[0])
vetor1[0] = 100
print(vetor1)

vetor1[0] = "Novo elemento"

print(vetor1.shape)

vetor2 = np.arange(0., 4.5, .5)
print(vetor2)
print(vetor2.dtype)

print(np.shape(vetor2))

x = np.arange(1, 10, 0.25)
print(x)

print(np.zeros(10))

z = np.eye(3)
print(z)

d = np.diag(np.array([1,2,3,4]))
print(d)

c = np.array([1+2j, 3+4j, 5+6*1j])
print(c)

b= np.array([True, False, False, True])
print(b)

s = np.array(["python", "R", "Julia"])
print(s)

print(np.linspace(0,10))

print(np.linspace(0, 10, 15))
print(np.logspace(0, 5, 15))

matriz = np.array([[1,2,3], [4,5,6]])
print(matriz)

print(matriz.shape)
matriz1 = np.ones((2,3))
print(matriz1)

lista = [[13,81,22], [0,34,59], [21,48,94]]
matriz2 = np.matrix(lista)
print(matriz2)
print(type(matriz2))
print(np.shape(matriz2))

print(matriz2.size)
print(matriz2.dtype)
print(matriz2.itemsize)
print(matriz2.nbytes)
print(matriz2[2,1])
matriz2 [1,0] = 100
print(matriz2)

x = np.array([1,2])
y = np.array([1.0, 2.0])
z = np.array([1,2], dtype=np.float64)

print(x.dtype, y.dtype, z.dtype)

matriz3 = np.array([[24,76], [35,89]], dtype=float)
print(matriz3)
print(matriz3.itemsize)
print(matriz3.nbytes)
print(matriz3.ndim)
print(matriz3[1,1])
matriz3[1,1] = 100
print(matriz3)

print(np.random.rand(10))

import matplotlib.pyplot as plt

print(np.random.rand(10))
plt.show.hist(np.random.rand(1000))

print(np.random.rand(5,5))

imagem = np.random.rand(30,30)
plt.imshow(imagem, cmap = plt.cm.hot)
plt.colorbar()

import os

filename = os.path.join('iris.csv')
arquivo = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)
print(arquivo)

print(type(arquivo))

var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
plt.show(plt.plot(var1, var2, 'o', markersize=8, alpha=0.75))

A = np.array([15,23,63,94,75])

print(np.mean(A)) #Media
print(np.std(A)) #Desvio Padrao

print(np.var(A)) #Variancia

d = np.arange(1, 10)
print(d)

print(np.sum(d))
print(np.prod)
print(np.cumsum(d))

a = np.random.randn(400, 2)
m = a.mean(0)
print(m, m.shape)

plt.plot(a[:,0], a[:,1], 'o', markersize=5, alpha=0.50)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()

a = np.diag(np.arange(3))
print(a)

print(a[1,1])
print(a[1])

b = np.arange(10)
print(b)
print(b[2:9:3])

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a==b)
print(np.array_equal(a, b))

print(a.min())
print(a.max())

print(np.array([1,2,3])+1.5)
a = np.array([1.2,1.5,1.6,2.5,3.5,4.5])
b = np.around(a)

print(b)

B = np.array([1,2,3,4])
print(B)

C = B.flatten()
print(C)

v = np.array([1,2,3])
print(v[:, np.newaxis], v[:, np.newaxis].shape, v[np.newaxis, :].shape)
print(np.repeat(v, 3))
print(np.tile(v,3))
w = np.array([5,6])
np.concatenate((v,w), axis=0)

r = np.copy(v)
print(r)