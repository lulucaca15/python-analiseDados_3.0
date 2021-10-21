import pandas as pd

filename = open("arquivos/salarios.csv", "r")
data = filename.read()
rows = data.split("\n")
#print(rows)

filename = open("arquivos/salarios.csv", "r")
data = filename.read()
rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
#print (full_data)

count = 0
for row in full_data:
    count+=1
#print(count)

filename2 = open("arquivos/teste2.txt", "w")
data = filename2.write("Arquivo teste 2 gerado\nAdicionando conteúdo")
filename2.close()

arq4 = open("arquivos/teste2.txt", "r")
#print(arq4.read())
#print(arq4.read()) #Está no final do arquivo, nada para ler

arq4.seek(0)
#print(arq4.readlines())

#for line in open("arquivos/binary.csv"):
#    print(line)

filename = open("arquivos/binary.csv")
df = pd.read_csv(filename)
#print(df.head())

filename = open("arquivos/salarios.csv")
df = pd.read_csv(filename)
print(df.head())





