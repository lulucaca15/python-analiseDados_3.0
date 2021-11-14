import os

texto = "Cientista de dados é a profissão que mais tem crescido em todo o mundo"
arquivo = open(os.path.join("arquivos/cientista.txt"), ("w"))

for palavra in texto.split():
    arquivo.write(palavra+" ")
arquivo.close()

arquivo = open("arquivos/cientista.txt", "r")
content = arquivo.read()
print(content)
arquivo.close()

with open ("arquivos/cientista.txt", "r") as arquivo:
    content = arquivo.read()

print(len(content))

with open("arquivos/cientista.txt", "w") as arquivo:
    arquivo.write(texto[:21])
    arquivo.write("\n")
    arquivo.write(texto[:33])

arquivo = open("arquivos/cientista.txt", "r")
content = arquivo.read()
arquivo.close()

print(content)
