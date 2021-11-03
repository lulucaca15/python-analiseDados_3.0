from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome=nome
        self.cidade=cidade
        self.telefone=telefone
        self.email=email
    
    def __str__(self):
        return "Pessoa: Nome: %s, Cidade: %s, Telefone: %s, Email: %s" %(self.nome, \
        self.cidade, self.telefone, self.email)

    def __len__(self):
        return self.email

class Smartphone():
    
    def __init__(self, tamanho, interface):
        self.tamanho=tamanho
        self.interface=interface

class MP3Players(Smartphone):
    
    def __init__(self, capacidade, tamanho="pequeno", interface="led"):
        self.capacidade=capacidade
        Smartphone.__init__(self, tamanho, interface)
    
    def print_mp3player(self):
        print("Valores para o objeto criado: %s %s %s"  %(self.tamanho, self.interface, self.capacidade))
            


roc1 = Rocket(10, 15)
roc1.x
roc1.y
roc1.print_rocket()
roc1.move_rocket(12, 44)
roc1.print_rocket()

pessoa1 = Pessoa("Luca", "Porto alegre", "51-999539959", "lucaoliveira846@gmail.com")
smartphone = MP3Players("64GB")

print(str(pessoa1))

print(smartphone.print_mp3player())