filename = "arquivos/teste.txt"

arq3 = open(filename, "w")
arq3.write("Incluindo texto no arquivo criado")
arq3.close()

arq3 = open(filename, "r")
print(arq3.read())
arq3.close()