class Livro():

    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("COntrutor chamado para criar um objeto desta classe")

    def imprime(self):
        print("Foi criado um livro %s e ISBN %d" %(self.titulo, self.isbn))



livro1 = Livro()
print(type(livro1))

print(livro1.titulo)
print(livro1.isbn)

livro1.imprime()
#########################################################

livro2 = Livro("A menina", 10294)
livro2.imprime()


class Cachorro():
    def __init__(self, raca, idade):
        self.raca = raca
        self.idade = idade

Rex = Cachorro("Bulldog", 5)
print(Rex.raca)

hasattr(Rex, "raca")
setattr(Rex, "raca", "Vira-lata")
print(Rex.raca)
print(getattr(Rex, "idade"))
delattr(Rex, "idade")
print(Rex.idade)

print("##############################################")

class Animal():
    def __init__(self):
        print("Animal Criado")
    
    def Identif(self):
        print("Animal")

    def comer(self):
        print("Comendo")

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")

    def Identif(self):
        print("Cachorro")

    def latir(self):
        print("Au au")

rex = Cachorro()
rex.Identif()
rex.comer()
rex.latir()