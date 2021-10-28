lista = [2,4,6]
print(list(map(lambda x: x**3, lista)))

palavras = "A Data Science Academy oferece os melhores cursos de análise de dados do Brasil".split()
print(list(map(lambda x: [x.upper(), x.lower(), len(x)], palavras)))

matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)

def quadrado(x):
    if x == 0:
        print("0")
    else:
        print(x**2)
    cubo(x)

def cubo(x):
    if x == 0:
        print("0")
    else:
        print(x**3)

lista = [0, 1, 2, 3, 4]

for i in map(quadrado, lista):
    i

listaA = [2, 3, 4]
listaB = [10, 11, 12]

print(list(map(lambda x,y: x**y, listaA, listaB)))

list(filter((lambda x: x < 0), range(-5,5)))

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print (list(filter(lambda x: x in a, b)))

import time
print (time.strftime("%d/%m/%Y %H:%M"))


dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

dict3 = trocaValores(dict1, dict2)
print(dict3)

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for indice, valor in enumerate(lista):
    if indice>5:
        print(valor)
