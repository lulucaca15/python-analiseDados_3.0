dia = input("Qual dia da semana é Hoje?")

if(dia == "Sabado" or dia == "Domingo"):
   print("Dia de descanço")
else:
   print("voce precisa trabalhar")

frutas = ["uva", "Maça", "Ameixa", "Morango", "Abacaxi"]
if(frutas.__contains__("Morango")):
    print("Contem Morango")

for i in range(0, len(frutas)):
    if(frutas[i] == "Morango"):
        print("Contem Morango 2")  

lista=[]
tupla=(2,4,6,8)
for i in tupla:
    lista.append(i*2)

print(lista)

for i in range(100, 150, 2):
    print(i)

temperatura=40
while(temperatura>35):
    print(temperatura)
    temperatura-=1

contador=0
while(contador < 100):
    if(contador == 23):
        break
    print(contador)
    contador+=1

lista=[]
var=4
while(var <= 20):
    if(var %2 == 0):
        lista.append(var)
    var+=1

print(lista)

lista=[]
nums = range(5, 45, 2)
print(list(nums))

temperatura = float(input('Qual a temperatura? '))
if (temperatura > 30):
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
numR = frase.count('r')
print(numR)
