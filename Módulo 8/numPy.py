import numpy as np

#print(np.__version__)print

#print(help(np.array))

vetor1 = np.array([0,1,2,3,4,5,6,7,8])
#print(vetor1)
#print(type(vetor1))

#print(vetor1.cumsum())

lst = [0,1,2,3,4,5,6,7,8]
#print(lst)

#print(type(lst))

#print(vetor1[0])
vetor1[0] = 100
#print(vetor1)

#vetor1[0] = "Novo elemento" Not Possible

#print(vetor1.shape)

vetor2 = np.arange(0., 4.5, .5)
#print(vetor2)
#print(vetor2.dtype)

#print(np.shape(vetor2))

x = np.arange(1, 10, 0.25)
#print(x)

#print(np.zeros(10))

z = np.eye(3)
#print(z)

d = np.diag(np.array([1,2,3,4]))
print(d)

c = np.array([1+2j, 3+4j, 5+6*1j])
#print(c)

b= np.array([True, False, False, True])
#print(b)

s = np.array(["python", "R", "Julia"])
#print(s)

#print(np.linspace(0,10))

#print(np.linspace(0, 10, 15))
#print(np.logspace(0, 5, 15))

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