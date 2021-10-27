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
