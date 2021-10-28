def fahrenheit(t):
    return ((float(9)/5)*t + 32)

def celsius(t):
    return (float(5)/9) * (t-32)

temperaturas = [0, 22.5, 40, 100]

print(map(fahrenheit, temperaturas))
print(list(map(fahrenheit, temperaturas)))

for temp in map(fahrenheit, temperaturas):
    print(temp)

print(map(celsius, temperaturas))
print(list(map(celsius, temperaturas)))

print(map(lambda x: (5.0/9) * (x-32), temperaturas))
print(list(map(lambda x: (5.0/9) * (x-32), temperaturas)))

a = [1,2,3,4]
b = [5,6,7,8]

print(list(map(lambda x,y: x+y, a,b)))

c = [9,10,11,12]

print(list(map(lambda x,y,z: x+y+z, a,b,c)))

########################################

from functools import reduce

lista = [47,11,42,13]
print(lista)

def soma(a,b):
    x = a+b
    return x

print(reduce(soma, lista))

print(reduce(lambda x,y: x+y, lista))

max_find = lambda a,b: a if (a>b) else b
print(type(max_find))
print(reduce(max_find, lista))

###########################################

def verificaPar(num):
    if num %2 == 0:
        return True
    else:
        return False

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

print(filter(verificaPar, lista))
print(list(filter(verificaPar, lista)))
print(list(filter(lambda x: x%2==0, lista)))
print(list(filter(lambda num: num>8, lista)))

#############################################

lista = [x for x in "python"]
print(lista)

print(type(lista))

lista = [x**2 for x in range(0, 11)]
print(lista)

celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius]

print(fahrenheit)

lista = [ x**2 for x in [x**2 for x in range(11)]]
print(lista)

print('##############################################')

x = [1,2,3]
y=[4,5,6]

print(zip(x,y))
print(list(zip(x,y)))

print(list(zip("ABCD", "xy")))

a = [1,2,3]
b = [4,5,6,7,8]

print(list(zip(a,b)))

d1 = {"a" :1, "b" :2}
d2 = {"c" :4, "d" :5}

print(list(zip(d1,d2)))
print(list(zip(d1,d2.values())))

def trocaValores(d1, d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp


print(trocaValores(d1, d2))

print('##############################################')

seq = ['a', 'b', 'c']

print(enumerate(seq))
print(list(enumerate(seq)))

for indice, valor in enumerate(seq):
    print(indice, valor)

for indice, valor in enumerate(seq):
    if indice >=2:
        break
    else:
        print(valor)

lista = ["marketing", "tecnologia", "business"]

for i, item in enumerate(lista):
    print(i, item)

for i, item in enumerate("Isso é um teste"):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)