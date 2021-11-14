import pandas as pd

def numPares():
    for i in range(0, 21, 2):
        print(i)

numPares()

def lowerCase(str):
    return str.lower()

print(lowerCase("MEU NOME E LUCA"))

def addDois(list):
    list.append(5)
    list.append(6)
    return list

print(addDois([1,2,3,4]))

def doisParam(str, *params):
    print(str)
    print(*params)

doisParam("Numeros ")
doisParam("Números ", [1,2,3,4,5])


soma= lambda x,y : x+y
print(soma(1,2))


total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2
    print ("Dentro da função o total é: ", total)
    return total


soma( 10, 20 )
print ("Fora da função o total é: ", total)

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x : (float(9)/5)*x + 32, Celsius)
print (list(Fahrenheit))

dic={1: "Um", 2:"Dois"}
print(dir(dic))

print(dir(pd))

file_name = "binary.csv"
def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
    
retornaArq(file_name)

listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)