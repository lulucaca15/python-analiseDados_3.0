import json

dict={"nome" : "Luca Zilio",
      "linguagem": "Python",
      "similiar" : ["c", "modulo4", "lisp"],
      "users" : 10000
}

for k,v in dict.items():
    print(k,v)

json.dumps(dict)

with open ("arquivos/dados.json", "w") as arquivo:
    arquivo.write(json.dumps(dict))

with open("arquivos/dados.json", "r") as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print (data)
print(data["nome"])

from urllib.request import urlopen

response = urlopen("https://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")
data = json.loads(response)[0]

print("Titulo: ", data["title"])
print("URL: ", data["url"])
print("Duracao: ", data["duration"])
print("Numero de visualizações: ", data["stats_number_of_plays"])

import os

arquivo_fonte = "arquivos/dados.json"
arquivo_destino = "arquivos/json_data.txt"

with open(arquivo_fonte, "r") as infile:
    text = infile.read()
    with open(arquivo_destino, "w") as outfile:
        outfile.write(text)

open(arquivo_destino, "w").write(open(arquivo_fonte, "r").read())

with open (arquivo_fonte, "r") as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

print(data)

