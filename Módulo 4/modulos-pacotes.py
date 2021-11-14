import math
from math import sqrt
import random
import statistics
import os
import sys
import urllib.request

print(dir(math))

print(math.sqrt(25))

print(sqrt(9))

help(sqrt)

print(random.choice(["Maça", "Banana", "Morango"]))
print(random.sample(range(100), 10))

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados))

print(statistics.median(dados))

print(os.getcwd())
print(dir(os))
print(sys.stdout.write("Testee"))

print(dir(sys))

resposta = urllib.request.urlopen("http://python.org")
print(resposta)

html = resposta.read()
print(html)

